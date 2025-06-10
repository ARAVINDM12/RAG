**📚 RAGFlow – AI-Powered Document Question Answering**

RAGFlow is a Retrieval-Augmented Generation (RAG) based chatbot app that allows users to upload or select files and ask questions about their contents. It uses LangChain, Google Gemini API, and FAISS for fast, context-specific responses powered by local vector search and LLMs.

**🤖 Smart PDF Assistant**

This project enables intelligent Q&A over documents using RAG techniques. Users can upload new PDFs or select from previously uploaded files and interact via a chatbot interface. The chatbot answers based on actual document content, offering context-aware responses. Additionally, it supports full conversation history viewing, chat/file deletion, and seamless document management.

**🖥️ Live App:** [RAGFlow on Streamlit](https://aravindm12-rag-main-xryndf.streamlit.app/)

**📦 Features**

  ✅ Upload and manage files
  
  ✅ Select from previously uploaded documents
  
  ✅ Ask natural language questions about document content
  
  ✅ Context-specific answers via Google Gemini API
  
  ✅ View complete chat history
  
  ✅ Delete chat conversations or uploaded files
  
  ✅ Easy-to-use Streamlit web interface

**🛠️ Tech Stack**

  Python 3.10+
  
  LangChain
  
  FAISS (vector store)
  
  Google Generative AI (google-generativeai)
  
  Streamlit
  
  PyPDF
  
  dotenv


**📁 Folder Structure**

RAGFlow/
├── main.py                # Streamlit Web App
├── rag_chat.py            # Core RAG functions (embedding, retrieval, QA)
├── utils.py               # Helper functions
├── .env                   # For storing Gemini API key
├── requirements.txt       # All Python dependencies
├── README.md              # You’re here!

**🚀 Setup Instructions**

1. Clone the Repository
   
  git clone https://github.com/ARAVINDM12/RAG.git

3. Install Dependencies

  pip install -r requirements.txt
  
4. Set Up API Key

  Create a .env file in the root directory with your Google Gemini API key:

  GEMINI_API_KEY=your_gemini_api_key_here
  
**✅ How to Use**
  
  🌐 Web UI (Streamlit)

  streamlit run main.py
  
  Upload or select a PDF file
  
  Ask questions in the chat input
  
  View responses and full chat history
  
  Use sidebar to delete chats or files

  **📄 Supported File Format**
  
  PDF (.pdf)
