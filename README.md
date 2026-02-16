Great — I will **only enhance**, not remove anything (demo video, image, etc stay untouched).
I’ll update it to reflect your **new architecture (Ollama + Evaluation pipeline + Local RAG benchmarking)** while keeping your existing sections intact.

Below is your **edited README** 👇

---

# 💡 AI DSA Assistant

# Flow Diagram

<img width="1160" height="564" alt="Gemini_Generated_Image_8teojf8teojf8teo" src="https://github.com/user-attachments/assets/cb263ac5-0eba-41ad-967c-a88708b8e4de" />

## Demo Video

[![Demo Video](https://img.shields.io/badge/Demo-Video-red)](https://drive.google.com/file/d/1ycbKrYXiXhbPhS4T9ffZnU-8iTVmRBkD/view?usp=sharing)

A RAG-based DSA code generator using LangChain, Gemini/Ollama, and FAISS with hybrid search (BM25 + FAISS Ensemble). Uploads DSA PDFs, indexes them, and generates structured solutions (Brute Force → Improved → Optimal).

---

## 📹 Demo Video

[Watch the demo video here](https://drive.google.com/file/d/1ycbKrYXiXhbPhS4T9ffZnU-8iTVmRBkD/view?usp=sharing)

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit** - Web UI
* **LangChain** - RAG framework
* **Ollama (Qwen / Mistral / Llama)** - Local LLM inference
* **Google Gemini API (optional)** - Cloud LLM support
* **FAISS** - Vector database for semantic search
* **BM25** (rank_bm25) - Keyword-based search
* **Ensemble Retriever** - Hybrid search combining BM25 and FAISS
* **Automated Evaluation Framework** - Retrieval & Generation scoring pipeline

---

## 🚀 Features

* **Hybrid Search**: Combines keyword-based (BM25) and semantic-based (FAISS) retrieval for improved accuracy
* **Multi-Language Support**: Supports C++, Java, and Python DSA problems
* **Structured Solutions**: Generates three approaches - Brute Force, Improved, and Optimal
* **RAG Pipeline**: Uses relevant context from DSA PDFs to generate grounded solutions
* **Local LLM Support**: Fully offline inference using Ollama models
* **Automated Evaluation**: Built-in benchmarking system to measure retrieval and generation quality
* **Streamlit UI**: Clean and intuitive web interface

---

## 📊 Evaluation Framework (NEW)

This project includes a **fully automated benchmarking pipeline** to measure real RAG performance instead of manual inspection.

### Evaluation Stages

**1️⃣ Retrieval Evaluation**

* Dataset of 50+ DSA problems
* Hybrid retriever returns top-k context
* Checks if important algorithmic keywords exist in retrieved chunks
* Produces Retrieval Hit Rate

**Result:**
📌 Retrieval Accuracy ≈ **49%**

---

**2️⃣ Generation Evaluation**
A separate judge LLM evaluates generated answers on:

* Relevance to the question
* Faithfulness to retrieved context
* Completeness of explanation
* Clarity of response

Each scored from 1 → 5

**Average Scores**

| Metric       | Score    |
| ------------ | -------- |
| Relevance    | 3.16 / 5 |
| Faithfulness | 3.17 / 5 |
| Completeness | 3.03 / 5 |
| Clarity      | 4.19 / 5 |

📌 Overall grounded response quality ≈ **68%**

---

### Evaluation Workflow

Dataset → Retriever → Context → Student LLM → Generated Answer → Judge LLM → Scoring → Report

This allows repeatable and objective RAG benchmarking.

---

## ▶️ Run Locally

### Prerequisites

* Python 3.10 or higher
* Ollama installed (recommended)
* (Optional) Google Gemini API key

### Installation

```bash
git clone https://github.com/Devamsingh09/AI-DSA-Assistant.git
cd AI-DSA-Assistant
pip install -r requirements.txt
```

(Optional — Gemini)

```bash
GOOGLE_API_KEY=your_api_key_here
```

### Run App

```bash
streamlit run app/main.py
```

The app will be available at `http://localhost:8501`

---

## 📁 Project Structure

```
AI-DSA-Assistant/
├── app/
│   ├── indexer.py        # Creates FAISS and BM25 indexes
│   ├── rag_engine.py     # Hybrid search implementation
│   ├── setup.py          # Configuration and constants
│   └── main.py           # Streamlit UI
│
├── evaluator/
│   ├── dataset.json      # 50+ DSA benchmark questions
│   ├── retrieval_eval.py # Retrieval quality scoring
│   ├── generation_eval.py# LLM judge scoring
│   └── run_all.py        # Complete evaluation pipeline
│
├── data/pdfs/            # DSA documents
├── faiss_indexes/        # Generated vector indexes
├── requirements.txt
└── README.md
```

---

## 🔧 How It Works

1. **Indexing**

   * PDFs split into chunks
   * Stored in FAISS (semantic) + BM25 (keyword)

2. **Hybrid Retrieval**

   * Ensemble Retriever combines both methods

3. **Context Generation**

   * Top relevant chunks retrieved

4. **Code Generation**

   * Local LLM generates structured solution

5. **Evaluation (Research Mode)**

   * Retriever accuracy measured
   * LLM judged by another LLM
   * Produces automated performance report

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

* LangChain for the RAG framework
* Google for the Gemini API
* Ollama for local LLM inference
* FAISS for efficient vector search
* Streamlit for the web interface

---

If you want, next I can also craft a **resume-optimized 2-line project description** recruiters instantly understand.
