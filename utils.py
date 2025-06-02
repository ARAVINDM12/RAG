from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import (
    PyPDFLoader,
    TextLoader,
    JSONLoader,
    UnstructuredWordDocumentLoader
)
import os

def load_and_split_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext == ".txt":
        loader = TextLoader(file_path, encoding="utf-8")
    elif ext == ".json":
        # Customize JSON loader depending on your structure
        loader = JSONLoader(
            file_path=file_path,
            jq_schema=".text",  # Update `.text` to match your JSON structure
            text_content=False
        )
    elif ext == ".docx":
        loader = UnstructuredWordDocumentLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return splitter.split_documents(docs)
