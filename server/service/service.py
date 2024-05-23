"""Abstract service class"""

from abc import ABC, abstractmethod
from typing import List

from component.model_runtime.schema.chat import ChatRequest


class Service(ABC):
    @abstractmethod
    async def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Embed a list of documents.

        :param texts: A list of document texts.
        :return: A list of embeddings for each document.
        """
        raise NotImplementedError

    @abstractmethod
    async def chat(self, request: ChatRequest):
        """
        Large model responds to user's dialogue
        :param request: A chat request for a conversational agent
        :return: Large model responds
        """
        raise NotImplementedError
