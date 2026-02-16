import pickle
from app.setup import SAVE_DIR, embedding_model, PDF_FILES
from app.indexer import build_index

from langchain_community.vectorstores import FAISS
from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever


def load_retriever(language: str):
    """Hybrid retriever: BM25 + FAISS"""

    faiss_path = SAVE_DIR / f"{language}_index"
    bm25_path = SAVE_DIR / f"{language}_bm25.pkl"

    if not faiss_path.exists() or not bm25_path.exists():
        build_index(language, str(PDF_FILES[language]))

    # Load FAISS
    vectorstore = FAISS.load_local(
        str(faiss_path),
        embedding_model,
        allow_dangerous_deserialization=True
    )
    faiss_retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    # Load BM25
    with open(bm25_path, "rb") as f:
        bm25_retriever = pickle.load(f)

    # Hybrid retrieval
    retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, faiss_retriever],
        weights=[0.5, 0.5]
    )

    return retriever
