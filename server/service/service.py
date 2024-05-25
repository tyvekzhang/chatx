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

    @abstractmethod
    async def crawl_document(self, url: str):
        """
        Crawling web page content from a URL and coexisting it in a vector database

        Args:
            url (str): A url starts with http(https)

        Returns:
            dict: A success response containing the added id in vector store.
        """
        raise NotImplementedError

    @abstractmethod
    async def clear_history(self) -> None:
        """
        Clear all chat history
        """
        raise NotImplementedError
