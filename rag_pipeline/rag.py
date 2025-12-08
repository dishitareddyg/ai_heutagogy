
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def get_rag_response(query):

    embedder = OllamaEmbeddings(model="nomic-embed-text")

    vectordb = Chroma(
        persist_directory="vector_store",
        embedding_function=embedder
    )

    retriever = vectordb.as_retriever()

    llm = ChatOllama(model="llama3.1")

    docs = retriever.get_relevant_documents(query)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
    Use the context below to answer the query.
    
    CONTEXT:
    {context}

    QUESTION: {query}
    """

    response = llm.predict(prompt)
    return response
