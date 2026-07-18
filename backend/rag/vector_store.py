from langchain_chroma import Chroma

from rag.embeddings import get_embedding_model

DB_PATH = "data/chroma"


def create_vector_store(chunks):

    db = Chroma.from_texts(
        texts=chunks,
        embedding=get_embedding_model(),
        persist_directory=DB_PATH
    )

    return db


def load_vector_store():

    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=get_embedding_model()
    )

    return db