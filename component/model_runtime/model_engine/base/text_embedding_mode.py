"""Model class for text embedding model."""

from abc import ABC, abstractmethod
from typing import List

from component.model_runtime.model_engine.base.base_model import BaseModel
from component.model_runtime.schema.enums import ModelType


class TextEmbeddingModel(BaseModel, ABC):
    """
    Model class for text embedding model.
    """

    model_type: ModelType = ModelType.TEXT_EMBEDDING

    @abstractmethod
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Embed a list of documents.

        :param texts: A list of document texts.
        :return: A list of embeddings for each document.
        """
        raise NotImplementedError

    @abstractmethod
    def embed_query(self, text: str) -> List[float]:
        """
        Embed a single query text.

        :param text: The query text.
        :return: The embedding as a list of floats.
        """
        raise NotImplementedError
