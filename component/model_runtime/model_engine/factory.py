"""Factory to build embedding model and llm"""

from component.model_runtime.model_engine.hugging_face.text_embedding import (
    HuggingFaceEmbeddingLoader,
)
from component.model_runtime.model_engine.ollama.llm import OllamaLLM
from component.model_runtime.model_engine.tongyi.llm import TongyiLLM
from component.model_runtime.model_engine.tongyi.text_embedding import (
    TongyiEmbeddingLoader,
)
from config.config import configs


async def get_embeddings_model():
    """
    Asynchronously gets the text embedding model based on configuration.

    Returns:
        TongyiEmbeddingLoader if online, else HuggingFaceEmbeddingLoader.
    """
    if configs.online:
        textEmbeddingModel = TongyiEmbeddingLoader()
    else:
        textEmbeddingModel = HuggingFaceEmbeddingLoader(configs=configs)
    return textEmbeddingModel


async def get_llm_model():
    """
    Asynchronously gets the large language model (LLM) based on configuration.

    Returns:
        TongyiLLM if online, else OllamaLLM.
    """
    if configs.online:
        llm = TongyiLLM()
    else:
        llm = OllamaLLM()
    return llm
