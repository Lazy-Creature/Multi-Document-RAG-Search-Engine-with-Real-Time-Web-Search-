from backend.router import route_query
from backend.vector_store import load_index
from backend.web_search import tavily_search
from backend.config import GROQ_API_KEY
from langchain_groq import ChatGroq

llm= ChatGroq(api_key=GROQ_API_KEY, model="llama-3.3-70b-versatile")

def is_relevant(text, query):
    q_words= set(query.lower().split())
    t_words= set(text.lower().split())
    return len(q_words & t_words) >= 2     # minimum keyword overlap

def hybrid_answer(q):
    context= ""
    mode= "doc"

    # Try document search
    db= load_index()
    if db:
        docs= db.similarity_search(q, k=3)
        for d in docs:
            if is_relevant(d.page_content, q):
                context+= d.page_content + "\n"

    # If no relevant doc context → fallback to web
    if not context:
        mode= "web"
        web= tavily_search(q)
        for w in web:
            context+= w["content"] + "\n"

    prompt= f"""
Answer clearly and simply using this context:

{context}

Question:
{q}
"""
    answer= llm.invoke(prompt).content
    return answer, [], mode
