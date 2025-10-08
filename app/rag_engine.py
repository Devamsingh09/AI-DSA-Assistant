import os
from langchain_community.vectorstores import FAISS

from app.setup import SAVE_DIR, embedding_model, PDF_FILES

from app.indexer import build_index


def load_index(language: str):
    """Load FAISS index; build if not found."""
    index_path = os.path.join(SAVE_DIR, f"{language}_index")

    if not os.path.exists(index_path):
        # Build it from PDF
        build_index(language, PDF_FILES[language])

    return FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)
