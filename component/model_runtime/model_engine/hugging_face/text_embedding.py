"""HuggingFaceEmbedding model to generate embedding for text(s)"""

from typing import List

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.embeddings import Embeddings

from component.model_runtime.model_engine.base.text_embedding_mode import (
    TextEmbeddingModel,
)


class HuggingFaceEmbeddingLoader(TextEmbeddingModel, Embeddings):
    def __init__(self, configs):
        """
        Initialize the HuggingFaceEmbeddingLoader with the provided configs.

        :param configs: The configuration object.
        """
        self.configs = configs

    def validate_credentials(self, model: str, credentials: dict) -> None:
        """
        Validate model credentials

        :param model: model name
        :param credentials: model credentials
        :return:
        """
        pass

    def get_num_token(self, text: str) -> int:
        """
        This method is used to obtain the number of tokens of the specified text.

        Parameters:
        - text (str): The text to be processed.

        Returns:
        The specific number of tokens.
        """
        pass

    def get_embeddings_model(self) -> HuggingFaceEmbeddings:
        """
        Asynchronously load and return a HuggingFaceEmbeddings object.

        Returns:
            HuggingFaceEmbeddings: A HuggingFaceEmbeddings object loaded with the specified model_runtime and device.
        """
        return HuggingFaceEmbeddings(
            model_name=self.configs.embedding_model_path,
            model_kwargs={"device": self.configs.device},
        )

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Embed a list of documents.

        :param texts: A list of document texts.
        :return: A list of embeddings for each document.
        """
        embeddings: HuggingFaceEmbeddings = self.get_embeddings_model()
        return embeddings.embed_documents(texts=texts)

    def embed_query(self, text: str) -> List[float]:
        """
        Embed a single query text.

        :param text: The query text.
        :return: The embedding as a list of floats.
        """
        embeddings: HuggingFaceEmbeddings = self.get_embeddings_model()
        return embeddings.embed_query(text=text)
