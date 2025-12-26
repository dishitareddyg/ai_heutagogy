
from rag.loader import load_documents
from rag.vectorstore import get_vectorstore

def build():
    docs = load_documents()
    vectordb = get_vectorstore()
    vectordb.add_documents(docs)
    vectordb.persist()

if __name__ == "__main__":
    build()
