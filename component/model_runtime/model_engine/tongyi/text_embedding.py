"""TongyiEmbedding model to generate embedding for text(s)"""

from typing import List

import dashscope
from dashscope import TextEmbedding
from langchain_core.embeddings import Embeddings

from component.model_runtime.model_engine.base.text_embedding_mode import (
    TextEmbeddingModel,
)
from config.config import configs

dashscope.api_key = configs.dashscope_api_key


class TongyiEmbeddingLoader(TextEmbeddingModel, Embeddings):
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

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Embed a list of documents.

        :param texts: A list of document texts.
        :return: A list of embeddings for each document.
        """
        rsp = TextEmbedding.call(
            model=TextEmbedding.Models.text_embedding_v1, input=texts
        )

        embeddings = [record["embedding"] for record in rsp.output["embeddings"]]
        return embeddings if isinstance(texts, list) else embeddings[0]

    def embed_query(self, text: str) -> List[float]:
        """
        Embed a single query text.

        :param text: The query text.
        :return: The embedding as a list of floats.
        """
        return self.embed_documents(text)
