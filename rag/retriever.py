'''from sentence_transformers import SentenceTransformer, util
from .loader import load_documents

# Load embedding model ONCE
model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text, chunk_size=300, overlap=50):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)

    return chunks


def build_knowledge_base():
    documents = load_documents()

    chunks = []
    for doc in documents:
        chunks.extend(chunk_text(doc))

    embeddings = model.encode(chunks, convert_to_tensor=True)

    return chunks, embeddings


def retrieve_context(query, top_k=3):
    if not query or not query.strip():
        return ""

    chunks, embeddings = build_knowledge_base()

    query_embedding = model.encode(query, convert_to_tensor=True)

    scores = util.cos_sim(query_embedding, embeddings)[0]
    top_results = scores.topk(k=top_k)

    retrieved = [chunks[idx] for idx in top_results.indices]

    return "\n\n".join(retrieved)
'''