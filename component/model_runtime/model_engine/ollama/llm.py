import requests

from component.model_runtime.model_engine.base.llm_model import LargeLanguageModel
from component.prompt.prompt import EMPTY_TEMPLATE
from config.config import configs


class OllamaLLM(LargeLanguageModel):
    headers = {"Content-Type": "application/json"}
    options = {"seed": 101, "temperature": 0}

    def generate(self, question: str, **kwargs) -> str:
        """
        Generate a response for a given prompt with a provided model.
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
            model = configs.llm_model
        data = {
            "model": model,
            "prompt": content,
            "stream": False,
            "options": self.options,
        }
        endpoint_url = configs.endpoint_url + "api/generate"
        response = requests.post(
            endpoint_url,
            headers=self.headers,
            json=data,
            timeout=(10, 300),
            stream=False,
        )
        response_json = response.json()
        return response_json["response"]

    def chat(self, question: str, **kwargs) -> str:
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
            model = configs.llm_model

        if "stream" in kwargs:
            stream = kwargs["stream"]
        else:
            stream = False
        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": content},
                {"role": "user", "content": question},
            ],
            "stream": stream,
            "options": self.options,
        }
        endpoint_url = configs.endpoint_url + "api/chat"
        return requests.post(
            endpoint_url,
            headers=self.headers,
            json=data,
            timeout=(10, 300),
            stream=False,
        )

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
