from backend.rag.vector_store import load_vector_store


def get_retriever(k=5):
    """
    Returns a retriever that fetches the top-k
    most relevant chunks.
    """

    db = load_vector_store()

    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )

    return retriever