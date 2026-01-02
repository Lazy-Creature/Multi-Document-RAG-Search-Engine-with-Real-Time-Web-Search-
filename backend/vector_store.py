import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings= HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def index_documents(chunks):
    db= FAISS.from_documents(chunks, embeddings)
    db.save_local("faiss_index")

def load_index():
    if not os.path.exists("faiss_index"):
        return None
    return FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

