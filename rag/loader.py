from pathlib import Path

def load_documents():
    docs = []

    base_path = Path(__file__).resolve().parent.parent / "data" / "docs"

    for file in base_path.glob("*.md"):
        docs.append(file.read_text(encoding="utf-8"))

    print("Loaded documents:", len(docs))
    return docs


if __name__ == "__main__":
    docs = load_documents()
    print("First document preview:")
    print(docs[0][:200] if docs else "No documents found")
