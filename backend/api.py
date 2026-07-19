from backend.rag.retriever import get_retriever
from backend.gemini.gemini_client import ask_gemini

def chat_with_ai(question):
    """
    Retrieves relevant context using RAG and
    generates an answer using Gemini.
    """

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    answer = ask_gemini(
        question=question,
        context=context
    )

    return answer