import sys
import os


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

# Initialize session state
if 'docs' not in st.session_state:
    st.session_state['docs'] = None
if 'show_source' not in st.session_state:
    st.session_state['show_source'] = False
if 'code_generated' not in st.session_state:
    st.session_state['code_generated'] = False
if 'response' not in st.session_state:
    st.session_state['response'] = None

col1, col2 = st.columns(2)

with col1:
    if st.button("See Source"):
        if user_query.strip():
            vector_db = load_index(language.lower())
            docs = vector_db.similarity_search(user_query, k=10)
            st.session_state['docs'] = docs
            st.session_state['show_source'] = True
        else:
            st.warning("Please enter a query!")

with col2:
    if st.button("Generate Code"):
        if user_query.strip():
            if st.session_state['docs'] is None:
                vector_db = load_index(language.lower())
                docs = vector_db.similarity_search(user_query, k=10)
                st.session_state['docs'] = docs
            docs = st.session_state['docs']
            context = "\n".join([doc.page_content for doc in docs[:3]])

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

            st.session_state['response'] = response
            st.session_state['code_generated'] = True
        else:
            st.warning("Please enter a query!")

# Display source if requested
if st.session_state['show_source'] and st.session_state['docs'] is not None:
    docs = st.session_state['docs']
    st.subheader(f"🔍 Found {len(docs)} relevant documents from PDFs, showing top 3:")
    for i, doc in enumerate(docs[:3], 1):
        page_num = doc.metadata.get('page', 'N/A')
        st.write(f"**Snippet {i} (Page {page_num}):**")
        st.text_area(f"Context {i}", doc.page_content, height=100, disabled=True)

# Display code if generated
if st.session_state['code_generated'] and st.session_state['response'] is not None:
    content = st.session_state['response'].content

    # Split the content into three parts: Brute Force, Improved, Optimal
    if "**Improved:**" in content and "**Optimal:**" in content:
        parts = content.split("**Improved:**")
        brute_part = parts[0].replace("**Brute Force:**", "").strip()
        remaining = parts[1].split("**Optimal:**")
        improved_part = remaining[0].strip()
        optimal_part = remaining[1].strip()

        # Display each part separately
        st.subheader("🔹 Brute Force Approach:")
        st.code(brute_part, language.lower(), line_numbers=True)

        st.subheader("🔹 Improved Approach:")
        st.code(improved_part, language.lower(), line_numbers=True)

        st.subheader("🔹 Optimal Approach:")
        st.code(optimal_part, language.lower(), line_numbers=True)
    else:
        # Fallback if parsing fails
        st.subheader("🔹 AI-Generated Code:")
        st.code(content, language.lower())
