from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings

BASE_DIR = Path(__file__).resolve().parent.parent

# Directory to save FAISS indexes
SAVE_DIR = BASE_DIR / "faiss_indexes"
SAVE_DIR.mkdir(exist_ok=True)

# PDF files for each language
PDF_FILES = {
    "cpp": BASE_DIR / "data" / "pdfs" / "dsa_cpp.pdf",
    "java": BASE_DIR / "data" / "pdfs" / "dsa_java.pdf",
    "python": BASE_DIR / "data" / "pdfs" / "dsa_python.pdf",
}

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
