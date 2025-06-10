# **📚 RAG – AI-Powered Document Question Answering**
An advanced Retrieval-Augmented Generation (RAG) based chatbot app that allows users to upload or select files and ask questions about their     contents. It uses LangChain, Google Gemini API, and FAISS for fast, context-specific responses powered by local vector search and LLMs.


**🤖 Smart Multi-Document Assistant**

    This project enables users to:
    
    Upload and manage a wide range of document types
    
    Select from previously uploaded documents
    
    Ask questions about the content using natural language
    
    Receive context-specific, AI-generated answers
    
    View and manage full chat history
    
    Clear vector database (FAISS index) and reset cache as needed
    
    Delete individual chats and documents
    
    Built with Streamlit, it offers a simple yet powerful UI for document-based AI interactions.

    
**🖥️ Live App:** (https://aravindm12-rag-main-xryndf.streamlit.app/)


**📦 Features**
  
    ✅ Upload and manage files
    
    ✅ Select from previously uploaded documents
    
    ✅ Ask natural language questions about document content
    
    ✅ Context-specific answers via Google Gemini API
    
    ✅ View complete chat history
    
    ✅ Delete chat conversations or uploaded files
    
    ✅ Store vector embeddings using FAISS for fast retrieval
    
    ✅ Option to clear/reset the FAISS vector cache
    
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

    RAG/
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
  
    **🌐 Web UI (Streamlit)**
  
    streamlit run main.py
    
    Upload or select a PDF file
    
    Ask questions in the chat input
    
    View responses and full chat history
    
    Use sidebar to delete chats or files

  **📄 Supported File Formats**
    
    📄 PDF (.pdf)
    
    📝 Word Documents (.docx)
    
    📂 JSON Files (.json)
    
    📃 Plain Text (.txt)**📄 Supported File Format**
    
  
