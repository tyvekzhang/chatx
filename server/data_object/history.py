"""History data object"""

from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, Column, String
from sqlmodel import SQLModel, Field


class ChatHistoryDO(SQLModel, table=True):
    __tablename__ = "chat_history"
    __table_args__ = {"comment": "Chat history data table"}

    id: int = Field(
        default=None,
        primary_key=True,
        index=True,
        nullable=False,
        sa_type=BigInteger,
    )

    query_history: str = Field(
        sa_column=Column(String(512), nullable=True, comment="query_history")
    )

    create_time: Optional[datetime] = Field(default_factory=datetime.now)
    update_time: Optional[datetime] = Field(
        default_factory=datetime.now, sa_column_kwargs={"onupdate": datetime.now}
    )
