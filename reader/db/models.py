from sqlalchemy import VARCHAR, Boolean, Column, DateTime, ForeignKey, Integer, String, Text, sql
from sqlalchemy.orm import relationship

from reader.db.base_class import Base


class UserProfile(Base):
    """
    One
    """

    __tablename__ = "user"

    id = Column(VARCHAR(64), primary_key=True, index=True)
    name = Column(String, default=None)
    weixin = Column(VARCHAR(50), default=None)
    gender = Column(Integer, default=0)
    is_friend = Column(Boolean, default=None)


class ChatHistory(Base):
    """one to many"""

    __tablename__ = "history"

    msg_id = Column(String, default=None)
    filename = Column(Text, default=None)
    text = Column(Text, default=None)
    type = Column(Integer, default=None)
    from_id = Column(VARCHAR(50), default=None)
    room_id = Column(VARCHAR(50), default=None)
    to_id = Column(VARCHAR(50), default=None)
    mention_ids = Column(Text, default=None)
    timestamp = Column(Integer, default=None)
    created_at = Column(DateTime(timezone=True), server_default=sql.func.now(), default=sql.func.now())
