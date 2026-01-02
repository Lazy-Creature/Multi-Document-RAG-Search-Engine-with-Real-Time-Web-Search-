from langchain_community.document_loaders import PyPDFLoader, TextLoader, WikipediaLoader

def load_pdfs(paths):
    docs=[]
    for p in paths: docs+=PyPDFLoader(p).load()
    return docs

def load_txt(path): return TextLoader(path).load()
def load_wiki(topic): return WikipediaLoader(query=topic,load_max_docs=2).load()
