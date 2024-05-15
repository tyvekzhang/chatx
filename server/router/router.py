"""Routing of this project"""

from typing import List

from fastapi import APIRouter

from model.embedding.embedding import get_embeddings_model
from server.enums.response import ResponseCode
from server.result import result

router = APIRouter()


@router.get("/liveness")
async def liveness():
    """
    Check the system's live status.

    Returns:
        dict: A status object with a 'code' and a 'msg' indicating liveness.
    """
    return {"code": ResponseCode.SUCCESS.code, "msg": "hi"}


@router.post("/embedding")
async def embedding(texts: List[str]):
    """
    Generate embedding for texts.

    Returns:
        dict: A status object with a 'code' and a 'msg' for texts embedding.
    """
    embeddings = get_embeddings_model()
    return result.success(embeddings.embed_documents(texts))
