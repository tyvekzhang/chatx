"""Model class for text rerank model."""

from abc import ABC

from component.model_runtime.model_engine.base.base_model import BaseModel
from component.model_runtime.schema.enums import ModelType


class RerankModel(BaseModel, ABC):
    """
    Model class for text rerank model.
    """

    model_type: ModelType = ModelType.RERANK
