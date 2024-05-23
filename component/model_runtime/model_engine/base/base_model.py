"""Base class for all models."""

from abc import ABC, abstractmethod
from typing import Any

from component.model_runtime.schema.enums import ModelType


class BaseModel(ABC):
    """
    Base class for all models.
    """

    model_type: ModelType
    model_config: Any

    @abstractmethod
    def validate_credentials(self, model: str, credentials: dict) -> None:
        """
        Validate model credentials

        :param model: model name
        :param credentials: model credentials
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def get_num_token(self, text: str) -> int:
        """
        This method is used to obtain the number of tokens of the specified text.

        Parameters:
        - text (str): The text to be processed.

        Returns:
        The specific number of tokens.
        """
        raise NotImplementedError
