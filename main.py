import streamlit as st
import tempfile
from utils import load_and_split_file
from rag_chat import create_vector_store, build_qa_chain,load_vector_store,VECTOR_DIR
import os
import shutil
import hashlib


st.set_page_config(page_title="📚 FILE Q&A Chatbot")

FILE_DIR = "uploaded_files"
VECTOR_DIR = "vector_store"

os.makedirs(FILE_DIR, exist_ok=True)
os.makedirs(VECTOR_DIR, exist_ok=True)

st.title("📄 Chat with your FILE")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if "all_history" not in st.session_state:
    st.session_state["all_history"] = []
    
st.sidebar.header("Saved Files")
supported_exts = [".pdf", ".txt", ".docx", ".json"]
saved_files = [f for f in os.listdir(FILE_DIR) if os.path.splitext(f)[1].lower() in supported_exts]
selected_files = st.sidebar.multiselect("Select saved files to chat with", saved_files)
for file in saved_files:
    if st.sidebar.button(f"🗑 Delete {file}"):
        file_path = os.path.join(FILE_DIR, file)
        vectorstore_path = os.path.join(VECTOR_DIR, os.path.splitext(file)[0])
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(vectorstore_path):
            shutil.rmtree(vectorstore_path)
        st.success("Deleted! Please refresh the page to see updated list.")
# Add the Clear Cache button here
if st.button("Clear Vector Store Cache"):
    if os.path.exists(VECTOR_DIR):
        shutil.rmtree(VECTOR_DIR)
        st.success("Vector store cache cleared! Please refresh the page.")
    else:
        st.info("No vector store cache found to clear.")

def load_multiple_files(file_list):
    all_docs = []
    for file in file_list:
        file_path = os.path.join(FILE_DIR, file)
        docs = load_and_split_file(file_path)
        all_docs.extend(docs)
    return all_docs

def get_combined_vectorstore_path(file_list):
    joined_names = "_".join(sorted(file_list))
    hashed = hashlib.md5(joined_names.encode()).hexdigest()
    return os.path.join(VECTOR_DIR, f"combined_{hashed}")

  
uploaded_files = st.file_uploader("Upload Files", type=["pdf", "txt", "docx", "json"], accept_multiple_files=True)
if uploaded_files:
    file_names = []
    for uploaded_file in uploaded_files:
        save_path = os.path.join(FILE_DIR, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        file_names.append(uploaded_file.name)
        st.success(f"Uploaded: {uploaded_file.name}")

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    if "all_history" not in st.session_state:
        st.session_state["all_history"] = []

    with st.spinner("Processing documents..."):
        combined_docs = load_multiple_files(file_names)
        vectorstore_path = get_combined_vectorstore_path(file_names)
        vectorstore = create_vector_store(combined_docs, vectorstore_path)

        qa_chain = build_qa_chain(vectorstore)
        st.success(f"Uploaded and processed {len(file_names)} FILEs")

    st.session_state.chain = qa_chain

if selected_files:
    vectorstore_path = get_combined_vectorstore_path(selected_files)

    if os.path.exists(vectorstore_path):
        with st.spinner(f"Loading vector store for selected FILEs..."):
            vectorstore = load_vector_store(vectorstore_path)
            qa_chain = build_qa_chain(vectorstore)
            st.session_state.chain = qa_chain
            st.success(f"Loaded vector store for selected FILEs!")
    else:
        with st.spinner("Creating vector store from selected FILEs..."):
            combined_docs = load_multiple_files(selected_files)
            vectorstore = create_vector_store(combined_docs, vectorstore_path)
            qa_chain = build_qa_chain(vectorstore)
            st.session_state.chain = qa_chain
            st.success("Created vector store for selected FILEs!")

query = st.text_input("Ask a question about the FILE:")

if query and "chain" in st.session_state:
    result = st.session_state.chain({
        "question": query,
        "chat_history": st.session_state["chat_history"]
    })
    answer = result["answer"]
    chat_history = result["chat_history"]
    st.session_state["chat_history"] = chat_history
    st.session_state["all_history"].append({"role": "user", "content": query})
    st.session_state["all_history"].append({"role": "assistant", "content": answer})
    st.chat_message("user").markdown(query)
    st.chat_message("assistant").markdown(answer)
else:
    if query:
        st.warning("Please upload a File or select a saved File to chat.")

if st.button("Show Full Chat History"):
    with st.expander("Full Chat History"):
        for msg in st.session_state.get("all_history", []):
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])