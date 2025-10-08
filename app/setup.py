from langchain_huggingface import HuggingFaceEmbeddings

# Directory to save FAISS indexes
SAVE_DIR = "faiss_indexes"

# PDF files for each language
PDF_FILES = {
    "cpp": "data/pdfs/dsa_cpp.pdf",
    "java": "data/pdfs/dsa_java.pdf",
    "python": "data/pdfs/dsa_python.pdf",
}

# Embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
