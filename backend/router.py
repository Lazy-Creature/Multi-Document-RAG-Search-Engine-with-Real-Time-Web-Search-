def route_query(q):
    q=q.lower()
    if "latest" in q or "today" in q or "current" in q: return "web"
    if "compare" in q: return "hybrid"
    return "doc"
