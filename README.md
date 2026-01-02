# 🧠Hybrid Multi-Document RAG Search Engine  
### Enterprise AI Copilot with FAISS, LangChain, Tavily & Streamlit

---

## 📌 Project Overview

GA02 is an enterprise-grade Hybrid RAG (Retrieval-Augmented Generation) system that allows users to build a private AI knowledge base from documents and combine it with real-time web knowledge.

It enables:
- Semantic document search
- Live web-based question answering
- Automatic fallback from documents to web
- Grounded, citation-aware AI answers

This architecture is inspired by Microsoft Copilot, Google NotebookLM, and Perplexity AI.

---

## 🚀 Features

- 📂 Upload and index multiple PDF documents  
- 🧠 FAISS vector database for semantic retrieval  
- 🌐 Tavily live web search integration  
- 🔀 Smart Hybrid RAG with automatic fallback  
- 💬 ChatGPT-style Streamlit UI  
- 🔐 Secure API key handling using `.env`  

---

## 🏗 Architecture
<img width="335" height="381" alt="image" src="https://github.com/user-attachments/assets/06fa942f-bc3d-4cf6-81a1-d0661c379020" />


---

## 🛠 Tech Stack

| Layer | Technology |
|------|------------|
Frontend | Streamlit |
LLM | Groq (LLaMA 3.3) |
Vector DB | FAISS |
Embeddings | HuggingFace |
Web Search | Tavily |
Orchestration | LangChain |

---

## 📂 Project Structure

GA02/
│
├── app.py
├── requirements.txt
├── .env
│
├── backend/
│ ├── config.py
│ ├── loader.py
│ ├── chunker.py
│ ├── vector_store.py
│ ├── web_search.py
│ ├── rag_engine.py
│ └── router.py
│
└── data/uploads/


---

## ⚙ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/GA02-Hybrid-RAG.git
cd GA02-Hybrid-RAG
```

2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Create .env
```bash
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```
5️⃣ Run Application
```bash
streamlit run app.py
```


<img width="772" height="478" alt="image" src="https://github.com/user-attachments/assets/82f90cad-f826-43b4-bedd-82ec0df4ee2c" />

🎓 Learning Outcomes

Hybrid RAG Architecture

Vector Databases (FAISS)

Live Web Search Integration

Enterprise AI Application Design


