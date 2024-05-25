from typing import Optional, List

from sqlalchemy import text
from sqlmodel import Session, select

from server.data_object.history import ChatHistoryDO
from component.vector_store.pg_vector import engine


async def add_chat_history(chatHistoryDO: ChatHistoryDO) -> ChatHistoryDO:
    """
    Add a new chat history record to the database.

    Args:
        chatHistoryDO (ChatHistoryDO): The chat history data object to be added.

    Returns:
        ChatHistoryDO: The added chat history data object.

    Raises:
        Exception: If any error occurs during the database operation.
    """
    with Session(engine) as session:
        try:
            session.add(chatHistoryDO)
            session.commit()
            session.refresh(chatHistoryDO)
            return chatHistoryDO
        except Exception as e:
            session.rollback()
            raise e


async def search_chat_history(limit: int) -> Optional[List[ChatHistoryDO]]:
    """
    Search and retrieve chat history records from the database.

    Args:
        limit (int): The maximum number of records to return.

    Returns:
        List[ChatHistoryDO]: A list of chat history data objects.
    """
    with Session(engine) as session:
        statement = (
            select(ChatHistoryDO)
                .order_by(ChatHistoryDO.update_time.desc())
                .limit(limit)
        )
        results = session.exec(statement)
        return results.all()


async def clear_all_chat_history() -> None:
    """
    Clear all chat history
    """
    with Session(engine) as session:
        session.execute(text('DELETE FROM chat_history'))
        session.commit()
