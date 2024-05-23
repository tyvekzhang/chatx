"""Chat schema"""

from typing import List

from pydantic import BaseModel

from config.config import configs


class ChatRequest(BaseModel):
    """
    A data model representing a chat request for a conversational agent.

    Attributes:
    question (str): The question or message that is being sent to the conversational agent.
    collection_name (str): Can choose use which collection to chat
    chat_history (List[str]): A list of strings representing the history of the conversation. Defaults to an empty list.
    limit (int): The maximum number of messages to be considered in the conversation. Defaults to 3.
    stream (bool): A flag indicating whether the chat should be processed as a continuous stream. Defaults to False.
    strict_model (bool): Defaults to False. If set to true, will return default words when can not find doc in vector store.
    """

    question: str
    collection_name: str = configs.default_collection_name
    chat_history: List[str] = []
    limit: int = 3
    stream: bool = False
    strict_model: bool = False
