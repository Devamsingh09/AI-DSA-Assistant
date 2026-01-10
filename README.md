# 💡 AI DSA Assistant
# Flow Diagram
<img width="1160" height="564" alt="Gemini_Generated_Image_8teojf8teojf8teo" src="https://github.com/user-attachments/assets/cb263ac5-0eba-41ad-967c-a88708b8e4de" />

## Demo Video
[![Demo Video](https://img.shields.io/badge/Demo-Video-red)](https://drive.google.com/file/d/1ycbKrYXiXhbPhS4T9ffZnU-8iTVmRBkD/view?usp=sharing)

A RAG-based DSA code generator using LangChain, Gemini, and FAISS with hybrid search (BM25 + FAISS Ensemble). Uploads DSA PDFs, indexes them, and generates structured solutions (Brute Force → Improved → Optimal).

## 📹 Demo Video

[Watch the demo video here](https://drive.google.com/file/d/1ycbKrYXiXhbPhS4T9ffZnU-8iTVmRBkD/view?usp=sharing)

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** - Web UI
- **LangChain** - RAG framework
- **Google Gemini API** - LLM for code generation
- **FAISS** - Vector database for semantic search
- **BM25** (via rank_bm25) - Keyword-based search
- **Ensemble Retriever** - Hybrid search combining BM25 and FAISS

## 🚀 Features

- **Hybrid Search**: Combines keyword-based (BM25) and semantic-based (FAISS) retrieval for improved accuracy
- **Multi-Language Support**: Supports C++, Java, and Python DSA problems
- **Structured Solutions**: Generates three approaches - Brute Force, Improved, and Optimal
- **RAG Pipeline**: Uses relevant context from DSA PDFs to generate accurate solutions
- **Streamlit UI**: Clean and intuitive web interface

## ▶️ Run Locally

### Prerequisites

- Python 3.10 or higher
- Google Gemini API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Devamsingh09/AI-DSA-Assistant.git
cd AI-DSA-Assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create a .env file in the root directory
GOOGLE_API_KEY=your_api_key_here
```

4. Run the application:
```bash
streamlit run main.py
```

The app will be available at `http://localhost:8501`

## 📁 Project Structure

```
AI-DSA-Assistant/
├── app/
│   ├── indexer.py      # Creates FAISS and BM25 indexes
│   ├── rag_engine.py   # Hybrid search implementation
│   └── setup.py        # Configuration and constants
├── data/
│   └── pdfs/           # DSA PDF documents
├── faiss_indexes/      # Generated vector indexes
├── main.py             # Streamlit application
├── requirements.txt    # Python dependencies
└── README.md
```

## 🔧 How It Works

1. **Indexing**: PDFs are loaded, split into chunks, and indexed using both FAISS (semantic) and BM25 (keyword-based)
2. **Hybrid Retrieval**: Ensemble Retriever combines results from both BM25 and FAISS with equal weights
3. **Context Generation**: Top relevant chunks are retrieved and used as context
4. **Code Generation**: Google Gemini generates structured solutions using the retrieved context

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- LangChain for the RAG framework
- Google for the Gemini API
- FAISS for efficient vector search
- Streamlit for the web interface
