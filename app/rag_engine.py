import os
import pickle
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever

from app.setup import SAVE_DIR, embedding_model, PDF_FILES
from app.indexer import build_index


def load_index(language: str):
    """Load FAISS index; build if not found."""
    index_path = os.path.join(SAVE_DIR, f"{language}_index")

    if not os.path.exists(index_path):
        # Build it from PDF
        build_index(language, PDF_FILES[language])

    return FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)


def load_bm25_retriever(language: str):
    """Load BM25 retriever; build if not found."""
    bm25_path = os.path.join(SAVE_DIR, f"{language}_bm25.pkl")

    if not os.path.exists(bm25_path):
        # Build it from PDF
        build_index(language, PDF_FILES[language])

    with open(bm25_path, 'rb') as f:
        return pickle.load(f)


def load_ensemble_retriever(language: str):
    """Load EnsembleRetriever combining FAISS and BM25."""
    faiss_vectorstore = load_index(language)
    bm25_retriever = load_bm25_retriever(language)

    # Create retrievers from FAISS
    faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": 3})

    # Ensemble with equal weights
    ensemble_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, faiss_retriever],
        weights=[0.5, 0.5]
    )

    return ensemble_retriever
