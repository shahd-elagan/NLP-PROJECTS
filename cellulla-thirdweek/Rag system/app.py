import streamlit as st
from rag.rag_pipeline import RAGPipeline

st.set_page_config(page_title="PDF + Text RAG")

st.title(" PDF & Text RAG System")

@st.cache_resource
def load_rag():
    return RAGPipeline()

rag = load_rag()

question = st.text_input("Ask a question")

if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = rag.ask(question)
        st.write(answer)
    else:
        st.warning("Please enter a question")
