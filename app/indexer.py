import os
import pickle
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever
from app.setup import PDF_FILES, embedding_model, SAVE_DIR


def build_index(language: str, pdf_path: str):
    """Create FAISS and BM25 indexes for a given language if not already built."""
    faiss_index_path = SAVE_DIR / f"{language}_index"
    bm25_index_path = SAVE_DIR / f"{language}_bm25.pkl"


    # If indexes already exist, skip building
    if os.path.exists(faiss_index_path) and os.path.exists(bm25_index_path):
        print(f"⚠️ Indexes for '{language}' already exist")
        return

    # Load and split PDF into chunks
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_docs = splitter.split_documents(docs)

    # Create FAISS index
    if not os.path.exists(faiss_index_path):
        vector_db = FAISS.from_documents(final_docs, embedding_model)
        vector_db.save_local(str(faiss_index_path))

        print(f"✅ FAISS index for '{language}' created at {faiss_index_path}")

    # Create BM25 index
    if not os.path.exists(bm25_index_path):
        bm25_retriever = BM25Retriever.from_documents(final_docs)
        with open(str(bm25_index_path), 'wb') as f:
            pickle.dump(bm25_retriever, f)
        print(f"✅ BM25 index for '{language}' created at {bm25_index_path}")
