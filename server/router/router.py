"""Routing of this project"""

from typing import List

from fastapi import APIRouter

from model.embedding.embedding import get_embeddings_model
from server.enums.response import ResponseCode
from server.result import result
from vector_store.pg_vector import add_documents, search_documents

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
    embeddings = await get_embeddings_model()
    return result.success(embeddings.embed_documents(texts))


@router.post("/documents")
async def add_docs(documents: List[str]):
    """
    Add a list of documents to the document store.

    Args:
        documents (List[str]): A list of document strings to be added.

    Returns:
        dict: A success response containing the added id in vector store.
    """
    return result.success(await add_documents(documents))


@router.post("/search")
async def search_docs(query: str):
    """
    Search for documents matching the given query.

    Args:
        query (str): The search query string.

    Returns:
        dict: A success response containing the top-k relevance docs.
    """
    return result.success(await search_documents(query))
