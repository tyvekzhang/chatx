"""Embedding model to generate embedding for text(s)"""

from langchain_core.embeddings import Embeddings

from langchain_community.embeddings import HuggingFaceEmbeddings

from config.config import configs


async def get_embeddings_model() -> Embeddings:
    """
    Asynchronously load and return a HuggingFaceEmbeddings object.

    Returns:
        Embeddings: A HuggingFaceEmbeddings object loaded with the specified model and device.
    """
    return HuggingFaceEmbeddings(
        model_name=configs.embedding_model_path, model_kwargs={"device": configs.device}
    )
