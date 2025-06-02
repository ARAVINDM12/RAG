import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores.faiss import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.2, google_api_key=GOOGLE_API_KEY)

# Embeddings
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

VECTOR_DIR = "vector_store"

def create_vector_store(documents, path):
    if not os.path.exists(path):
        os.makedirs(path)

    vectorstore = FAISS.from_documents(documents, embedding_model)
    vectorstore.save_local(path)
    return vectorstore

def load_vector_store(path):
    if os.path.exists(path):
        return FAISS.load_local(path, embedding_model, allow_dangerous_deserialization=True)
    return None

def build_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    prompt = PromptTemplate(
        input_variables=["context", "question", "chat_history"],
        template="""
        You are an intelligent assistant that answers questions strictly based on the given context.

        - Use only the information in the context to answer.
        - If unsure, say "I'm not sure based on the document."

        Context:
        {context}

        Chat History:
        {chat_history}

        Question:
        {question}

        Answer:
        """
            )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer")
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        output_key="answer",
        combine_docs_chain_kwargs={"prompt": prompt}
    )
    return qa_chain
