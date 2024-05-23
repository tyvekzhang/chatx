"""TongyiLLM implement LargeLanguageModel"""

from http import HTTPStatus

import dashscope
from dashscope import Generation

from component.model_runtime.model_engine.base.llm_model import LargeLanguageModel
from component.prompt.prompt import EMPTY_TEMPLATE
from config.config import configs

dashscope.api_key = configs.dashscope_api_key


class TongyiLLM(LargeLanguageModel):
    def generate(self, question: str, **kwargs):
        """
        Generate a response for a given prompt with a provided model.
        :param question: Chat message from user
        :param kwargs: Model config and other param
        :return: A message generated from llm
        """
        if "content" in kwargs:
            content = kwargs["content"]
        else:
            content = "You are a helpful assistant."

        if "model" in kwargs:
            model = kwargs["model"]
        else:
            model = "qwen-turbo"
        messages = [
            {"role": "system", "content": content},
            {"role": "user", "content": question},
        ]
        response = Generation.call(
            model=model, messages=messages, result_format="message"
        )
        if response.status_code == HTTPStatus.OK:
            return response.output.choices[0]["message"]["content"]

    def chat(self, question: str, **kwargs):
        """
        Generate the next message in a chat with a provided model.
        :param question: Chat message from user
        :param kwargs: Model config and other param
        :return: A message generated from llm
        """
        if "content" in kwargs:
            content = kwargs["content"]
        else:
            content = EMPTY_TEMPLATE

        if "model" in kwargs:
            model = kwargs["model"]
        else:
            model = "qwen-turbo"

        if "stream" in kwargs:
            stream = kwargs["stream"]
        else:
            stream = False
        messages = [
            {"role": "system", "content": content},
            {"role": "user", "content": question},
        ]
        return Generation.call(model=model, messages=messages, stream=stream)

    def validate_credentials(self, model: str, credentials: dict) -> None:
        """
        Validate model credentials

        :param model: model name
        :param credentials: model credentials
        :return:
        """

    def get_num_token(self, text: str) -> int:
        """
        This method is used to obtain the number of tokens of the specified text.

        Parameters:
        - text (str): The text to be processed.

        Returns:
        The specific number of tokens.
        """
