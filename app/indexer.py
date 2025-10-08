import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from app.setup import PDF_FILES, embedding_model, SAVE_DIR


def build_index(language: str, pdf_path: str):
    """Create FAISS index for a given language if not already built."""
    index_path = os.path.join(SAVE_DIR, f"{language}_index")

    # If index already exists, skip building
    if os.path.exists(index_path):
        print(f"⚠️ Index for '{language}' already exists at {index_path}")
        return

    # Load and split PDF into chunks
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_docs = splitter.split_documents(docs)

    # Create FAISS index
    vector_db = FAISS.from_documents(final_docs, embedding_model)
    vector_db.save_local(index_path)

    print(f"✅ {language.capitalize()} index created at {index_path}")
