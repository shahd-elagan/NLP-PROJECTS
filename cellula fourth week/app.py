


import streamlit as st
import sys
from rag_pipeline import generate
from main import explain  # use your existing explain function

st.set_page_config(page_title="RAG Code Assistant", layout="wide")
st.title("RAG Code Assistant")

query = st.text_area("Enter your programming query here:")

if st.button("Get Answer"):
    if query.strip() == "":
        st.warning("Please enter a query!")
    else:
        with st.spinner("Generating answer..."):
            # decide which pipeline to use
            # simple logic: if query contains "explain", call explain
            if "explain" in query.lower() or "describe" in query.lower():
                response = explain(query)
            else:
                response = generate(query)

        st.success("Answer:")
        st.code(response, language="python")