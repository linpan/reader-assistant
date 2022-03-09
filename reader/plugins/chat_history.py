"""Chat history plugin"""
import os
from dataclasses import dataclass, field
from typing import Any, List, Optional

from wechaty import Message, Wechaty, get_logger
from wechaty.plugin import WechatyPlugin, WechatyPluginOptions
from wechaty_puppet import FileBox, MessageType

from reader.db.base import Base, ChatHistory
from reader.db.session import async_engine, async_session

logger = get_logger(__name__)


@dataclass
class ChatHistoryPluginOptions(WechatyPluginOptions):
    """
    chat history plugin options paras
    """

    chat_history_database: str = field(default_factory=str)


class ChatHistoryPlugin(WechatyPlugin):
    """chat history plugin"""

    def __init__(self, options: Optional[ChatHistoryPluginOptions] = None):
        super().__init__(options)
        if options is None:
            options = ChatHistoryPluginOptions()
        self.chat_history_database = options.chat_history_database or "postgresql+asyncpg://hiro@localhost/history"

    @property
    def name(self) -> str:
        return "chat-history"

    async def init_plugin(self, wechaty: Wechaty) -> None:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def on_message(self, msg: Message) -> None:

        async with async_session() as session:
            async with session.begin():
                payload = msg.payload
                if not payload.text.startswith("<msg>"):
                    history = ChatHistory(
                        msg_id=msg.message_id,
                        text=payload.text if payload.text else None,
                        timestamp=payload.timestamp,
                        type=payload.type.value,
                        from_id=payload.from_id,
                        room_id=payload.room_id if payload.room_id else None,
                        to_id=payload.to_id if payload.to_id else None,
                        mention_ids=",".join(payload.mention_ids) if payload.mention_ids else None,
                    )
                    session.add(history)
            await session.commit()
        # for AsyncEngine created in function scope, close and
        # clean-up pooled connections
        await async_engine.dispose()


class HistoryPlugin:
    def __call__(self, *args, **kwargs) -> ChatHistoryPlugin:
        plugin = ChatHistoryPlugin()
        return plugin


chat_history = HistoryPlugin()()
