from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def get_vectorstore(documents):
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="data/chroma"
    )
    vectordb.persist()
    return vectordb
