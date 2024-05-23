"""Model class for large language model."""

from abc import ABC

from component.model_runtime.model_engine.base.base_model import BaseModel
from component.model_runtime.schema.enums import ModelType


class LargeLanguageModel(BaseModel, ABC):
    """
    Model class for large language model.
    """

    model_type: ModelType = ModelType.LLM

    def generate(self, question: str, **kwargs) -> str:
        """
        Generate a response for a given prompt with a provided model.
        :param question: Chat message from user
        :param kwargs: Model config and other param
        :return: A message generated from llm
        """
        raise NotImplementedError

    def chat(self, question: str, **kwargs) -> str:
        """
        Generate the next message in a chat with a provided model.
        :param question: Chat message from user
        :param kwargs: Model config and other param
        :return: A message generated from llm
        """
        raise NotImplementedError
