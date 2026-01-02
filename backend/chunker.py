from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter=RecursiveCharacterTextSplitter(chunk_size=700,chunk_overlap=150)
def chunk_docs(docs): return splitter.split_documents(docs)
