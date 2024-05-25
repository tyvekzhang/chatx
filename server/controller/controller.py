"""Controller of this project"""

from typing import List, Dict

from fastapi import APIRouter
from starlette.responses import StreamingResponse

from component.model_runtime.schema.chat import ChatRequest
from component.vector_store.pg_vector import add_documents
from server.enums.response import ResponseCode
from server.result import result
from server.service.impl.service_impl import get_service
from server.util.helper import handle_event_stream, handle_response

router = APIRouter()

headers = {"Content-Type": "text/event-stream; charset=utf-8"}


@router.get("/liveness")
async def liveness() -> Dict:
    """
    Check the system's live status.

    Returns:
        dict: A status object with a 'code' and a 'msg' indicating liveness.
    """
    return {"code": ResponseCode.SUCCESS.code, "msg": "Hi"}


@router.post("/chat")
async def chat(request: ChatRequest):
    """
    Endpoint to handle chat requests.

    Args:
        request (ChatRequest): Request object containing the chat input.

    Returns:
        dict: A dictionary containing the success status and the chat response from the LLM or StreamingResponse
    """
    chat_service = await get_service()
    response = await chat_service.chat(request)
    if request.stream:
        return StreamingResponse(content=handle_event_stream(response), headers=headers)
    return result.success(handle_response(response))


@router.post("/crawl")
async def crawl_docs(url: str):
    """
    Crawling web page content from a URL and coexisting it in a vector database

    Args:
        url (str): A url starts with http(https)

    Returns:
        dict: A success response containing the added id in vector store.
    """
    service = await get_service()
    return result.success(await service.crawl_document(url=url))


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


@router.post("/embedding")
async def embedding(texts: List[str]) -> Dict:
    """
    Generate embedding for texts.

    Returns:
        dict: A status object with a 'code' and a 'msg' for texts embedding.
    """
    embedding_service = await get_service()
    return result.success(await embedding_service.embed_documents(texts))


@router.delete("/history")
async def clear_history() -> Dict:
    """
    Clear all chat history
    :return: A status object with a 'code' and a 'msg' for success
    """
    service = await get_service()
    await service.clear_history()
    return result.success()
