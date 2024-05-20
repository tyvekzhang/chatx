import hashlib
from typing import List, Union

from langchain_core.documents import Document
from langchain_postgres import PGVector
from sqlalchemy import create_engine

from config.config import configs
from model.embedding.embedding import get_embeddings_model

engine = create_engine(configs.connection, pool_size=5, echo=True)
"""
Create a SQLAlchemy engine instance using the connection string from the configs module.
The echo=True parameter is used for logging all the SQL queries.
"""


async def get_vectorstore(collection_name: str = "wujilab") -> PGVector:
    """
    Get a PGVector instance for the specified collection name.

    Args:
        collection_name (str, optional): The name of the collection to use. Defaults to "wujilab".

    Returns:
        PGVector: An instance of the PGVector class.
    """
    embeddings = await get_embeddings_model()
    return PGVector(
        embeddings=embeddings,
        collection_name=collection_name,
        connection=engine,
        use_jsonb=True,
    )


async def score_threshold_process(
    doc_list: List[Document], score_threshold: float = 0.8, k: int = 3
):
    """
    Filter and limit the list of documents based on a score threshold and a maximum number of results.

    Args:
        doc_list (List[Document]): A list of (Document, similarity score) tuples.
        score_threshold (float, optional): The minimum similarity score to include a document. Defaults to 0.7.
        k (int, optional): The maximum number of documents to return. Defaults to 3.

    Returns:
        List[Document]: A list of (Document, similarity score) tuples filtered and limited based on the provided parameters.
    """
    if score_threshold is not None:
        doc_list = [
            (doc, similarity)
            for doc, similarity in doc_list
            if 1 - similarity > score_threshold
        ]
    return doc_list[:k]


async def add_documents(
    documents: Union[List[Document], List[str]], collection_name: str = "wujilab"
):
    """
    Add a list of documents to the specified collection.

    Args:
        documents (Union[List[Document], List[str]]): A list of Document objects or strings to be added.
        collection_name (str, optional): The name of the collection to add the documents to. Defaults to "wujilab".

    Returns:
        List[str]: A list of IDs for the added documents.
    """
    if isinstance(documents[0], str):
        transform_documents = []
        for doc in documents:
            hash_object = hashlib.sha256()
            hash_object.update(doc.encode("utf-8"))
            hash_value = hash_object.hexdigest()
            transform_documents.append(
                Document(page_content=doc, metadata={"id": hash_value})
            )
        documents = transform_documents
    vectorstore: PGVector = await get_vectorstore(collection_name)
    return await vectorstore.aadd_documents(documents)


async def search_documents(text: str, collection_name: str = "wujilab"):
    """
    Search for documents matching the given text query.

    Args:
        text (str): The text query to search for.
        collection_name (str, optional): The name of the collection to search in. Defaults to "wujilab".

    Returns:
        List[Document]: A list of (Document, similarity score) tuples matching the query.
    """
    vectorstore: PGVector = await get_vectorstore(collection_name)
    doc_list = await vectorstore.asimilarity_search_with_score(text)
    return await score_threshold_process(doc_list=doc_list)
