import os
from backend.config import TAVILY_API_KEY
from langchain_tavily import TavilySearch

os.environ["TAVILY_API_KEY"]= TAVILY_API_KEY

tool= TavilySearch(k=3)

def tavily_search(query):
    raw= tool.invoke({"query": query})

    normalized= []

    for item in raw:
        # Case 1: Already dict
        if isinstance(item, dict):
            title= item.get("title", "Tavily Result")
            content= item.get("content") or item.get("snippet") or ""
        else:
            # Case 2: Plain string
            title= "Tavily Result"
            content= str(item)

        normalized.append({
            "title": title,
            "content": content
        })

    return normalized
