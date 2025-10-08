import os
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv

# LangChain imports
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# ----------------- Setup -----------------
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Paths
base_dir = Path(os.getcwd())
pdf_dir = base_dir / "data" / "pdfs"
faiss_dir = base_dir / "faiss_indexes"
faiss_dir.mkdir(exist_ok=True)

# PDFs per language
pdf_files = {
    "cpp": pdf_dir / "dsa_cpp.pdf",
    "java": pdf_dir / "dsa_java.pdf",
    "python": pdf_dir / "dsa_python.pdf",
}


# ----------------- Cached Resources -----------------
@st.cache_resource
def load_embedding():
    """Load embedding model once and cache it."""
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


@st.cache_resource
def create_faiss_index(language: str, pdf_path: Path, embedding):
    """Create FAISS index from PDF and save locally (cached)."""
    loader = PyPDFLoader(str(pdf_path))
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_docs = splitter.split_documents(docs)

    vector_db = FAISS.from_documents(final_docs, embedding)
    index_path = faiss_dir / f"{language}_index"
    vector_db.save_local(str(index_path))

    return vector_db


@st.cache_resource
def load_faiss_index(language: str, embedding):
    """Load FAISS index if exists, else create it (cached)."""
    index_path = faiss_dir / f"{language}_index"
    if index_path.exists():
        return FAISS.load_local(str(index_path), embedding, allow_dangerous_deserialization=True)
    else:
        return create_faiss_index(language, pdf_files[language], embedding)


# ----------------- Streamlit App -----------------
st.title("💡 DSA Code Assistant (RAG + LLM)")

language = st.selectbox("Select Language:", ["CPP", "Java", "Python"])
user_query = st.text_area("Enter your DSA question:", "")

if st.button("Generate Code"):
    if user_query.strip():
        embedding = load_embedding()  # cached
        vector_db = load_faiss_index(language.lower(), embedding)  # cached

        docs = vector_db.similarity_search(user_query, k=3)
        context = "\n".join([doc.page_content for doc in docs])

        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

        response = llm.invoke([
            HumanMessage(content=f"""
            Please provide a solution in {language} using the given DSA context. Ensure the response follows these guidelines:

            1. Multiple Approaches: Present the solution in three forms—Brute Force, Improved, and Optimal.
            2. Readable & Clean Code: Ensure the code is well-structured, readable, and free from unnecessary characters.
            3. Comprehensive Explanation: Briefly explain the concept before providing the solution.
            4. Handling Incomplete Code: If an incomplete snippet is given, complete it logically.
            5. Politeness: Always conclude with: "Thank you from Devam😊".

            **DSA Context:**  
            {context}

            **User Query:**  
            {user_query}
            """)
        ])

        st.subheader("🔹 AI-Generated Code:")
        st.code(response.content, language.lower())
    else:
        st.warning("⚠️ Please enter a query!")
