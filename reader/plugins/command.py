"""command plugin"""
import re
from typing import Union

from wechaty import Contact, Message, Room, Wechaty, get_logger
from wechaty.plugin import WechatyPlugin
from wechaty_puppet import EventReadyPayload

from reader.db.session import async_engine

logger = get_logger(__name__)


class CommanderPlugin(WechatyPlugin):
    """chat history plugin"""

    @property
    def name(self) -> str:
        return "commond"

    async def init_plugin(self, wechaty: Wechaty) -> None:
        await super().init_plugin(wechaty)

    async def owner_friends(self) -> None:
        owner = self.bot.self()
        members = await owner.find_all()
        for member in members:
            print(
                member.name,
                "\t",
                "\t",
                member.get_id(),
                "\t",
                member.weixin(),
                "\t",
                member.is_friend(),
            )

    async def on_message(self, msg: Message) -> None:
        conversation: Union[Room, Contact] = msg.room() if msg.room() else msg.talker()
        text = msg.text()
        print(text)
        if "#7890#" in text:
            print("eee")
            all_rooms = await self.bot.Room.find_all()
            for room in all_rooms:
                topic = await room.topic()
                target = text.rsplit("#", maxsplit=1)[-1]
                if re.match(target, topic):
                    connect = self.bot.Room.load(room_id=room.room_id)
                    mm = await connect.member_list()
                    for m in mm:
                        print(m.name, "\t", m.get_id(), "\t", m.weixin())

        elif "#7891#" in text:
            await self.owner_friends()
        else:
            pass


class CommandPlugin:
    def __call__(self, *args, **kwargs) -> CommanderPlugin:
        plugin = CommanderPlugin()
        return plugin


command = CommandPlugin()()
