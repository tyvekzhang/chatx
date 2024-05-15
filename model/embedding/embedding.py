"""Embedding model to generate embedding for text(s)"""

from langchain_core.embeddings import Embeddings

from langchain_community.embeddings import HuggingFaceEmbeddings

from config.config import configs


def get_embeddings_model() -> Embeddings:
    return HuggingFaceEmbeddings(
        model_name=configs.embedding_model_path, model_kwargs={"device": configs.device}
    )


embeddings = get_embeddings_model()
