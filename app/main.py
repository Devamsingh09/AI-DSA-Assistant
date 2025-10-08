import sys
import os

# ✅ Ensure project root is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from app.rag_engine import load_index

st.set_page_config(page_title="DSA Code Assistant", page_icon="💡")
st.title("💡 DSA Code Assistant (RAG + LLM)")

language = st.selectbox("Select Language:", ["CPP", "Java", "Python"])
user_query = st.text_area("Enter your DSA question:")

if st.button("Generate Code"):
    if user_query.strip():
        vector_db = load_index(language.lower())
        docs = vector_db.similarity_search(user_query, k=3)
        context = "\n".join([doc.page_content for doc in docs])

        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=os.getenv("GOOGLE_API_KEY"))

        response = llm.invoke([
            HumanMessage(content=f"""
                You are a DSA and algorithm expert helping to solve coding problems with clear and structured explanations.

Please provide a solution in {language} using the given DSA context.

**Instructions:**
1. Provide **three versions**: Brute Force → Improved → Optimal.
2. Before each solution, write a **2–3 line explanation** (concise and practical, not verbose).
3. Code should be **clean, properly formatted, and minimal** (no unnecessary comments or extra text).
4. If the given snippet or context is incomplete, **logically complete it**.
5. End the answer politely with: “Thank you.”

**DSA Context:**
{context}

**User Query:**
{user_query}

            """)
        ])

        st.subheader("🔹 AI-Generated Code:")
        st.code(response.content, language.lower())
    else:
        st.warning("Please enter a query!")
