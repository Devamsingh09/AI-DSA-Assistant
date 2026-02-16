import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

from app.rag_engine import load_retriever


st.set_page_config(page_title="DSA Code Assistant", page_icon="💡")
st.title("💡 DSA Code Assistant (Hybrid RAG + Ollama)")

language = st.selectbox("Select Language:", ["cpp", "java", "python"])
user_query = st.text_area("Enter your DSA question:")

if st.button("Generate Code"):

    if not user_query.strip():
        st.warning("Please enter a query!")
        st.stop()

    # ---------- RETRIEVAL ----------
    with st.spinner("Retrieving relevant DSA concepts..."):
        retriever = load_retriever(language)
        docs = retriever.invoke(user_query)
        context = "\n\n".join([d.page_content for d in docs[:4]])

    # ---------- LLM ----------
    with st.spinner("Generating solution using local LLM..."):
        llm = ChatOllama(
            model="qwen2.5:7b-instruct",
            temperature=0,
        )

        messages = [
            HumanMessage(content=f"""
You are an expert DSA instructor.

Provide solution in {language}.

Rules:
1. Give 3 approaches → Brute Force → Better → Optimal
2. Short explanation before each
3. Format response in proper MARKDOWN
4. Use code blocks for code (```language)
5. End with: Thank you.

DSA Reference:
{context}

User Question:
{user_query}
""")
        ]

        # streaming output
        st.subheader("💡 Generated Solution")
        placeholder = st.empty()
        full_response = ""

        for chunk in llm.stream(messages):
            if chunk.content:
                full_response += chunk.content
                placeholder.markdown(full_response)