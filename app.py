import os
import warnings
warnings.filterwarnings("ignore", message="Advanced encoding /SymbolSetEncoding not implemented yet")

import streamlit as st
from backend.loader import load_pdfs
from backend.chunker import chunk_docs
from backend.vector_store import index_documents
from backend.rag_engine import hybrid_answer

# -------------------------------------------------
# Create upload folder safely
# -------------------------------------------------
os.makedirs("data/uploads", exist_ok=True)

st.set_page_config(page_title="GA02 Hybrid RAG", layout="wide")

# -------------------------------------------------
# Sidebar – Document Manager
# -------------------------------------------------
st.sidebar.title("📂 Document Manager")

uploaded_files= st.sidebar.file_uploader(
    "Upload PDF Documents",
    accept_multiple_files=True,
    type=["pdf"]
)

if st.sidebar.button("Index Documents"):
    if not uploaded_files:
        st.sidebar.warning("Please upload at least one PDF.")
    else:
        docs= []
        for f in uploaded_files:
            path= os.path.join("data/uploads", f.name)
            with open(path, "wb") as file:
                file.write(f.read())
            docs+=load_pdfs([path])

        chunks= chunk_docs(docs)
        index_documents(chunks)
        st.sidebar.success("Documents Indexed Successfully!")

# -------------------------------------------------
# Main Chat UI
# -------------------------------------------------
st.title("🔀 Hybrid Multi-Document RAG Search Engine")

if "chat_history" not in st.session_state:
    st.session_state.chat_history= []

user_query= st.chat_input("Ask your question here...")

if user_query:
    answer,sources,mode= hybrid_answer(user_query)

    st.session_state.chat_history.append({
        "question": user_query,
        "answer": answer,
        "mode": mode
    })

# -------------------------------------------------
# Display Chat History
# -------------------------------------------------
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(chat["question"])

    with st.chat_message("assistant"):
        st.write(chat["answer"])
        st.caption(f"Source: {chat['mode'].upper()}")
