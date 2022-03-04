"""
@齐晓瑞  @齐晓瑞 
"""
import asyncio
import os
from typing import Dict, Optional, Union

from wechaty import Contact, Room, Wechaty
from wechaty.user import Message
from wechaty_plugin_contrib.contrib import RoomInviterOptions, RoomInviterPlugin
from wechaty_plugin_contrib.matchers import MessageMatcher, RoomMatcher
from wechaty_puppet import FileBox

from reader.plugins.invite_rooms import room_invitor

os.environ["WECHATY_PUPPET_SERVICE_TOKEN"] = "puppet_paimon_72a5c28b-8ddf-4900-a42e-25518aa3cd76"


class ReaderBot(Wechaty):
    """
    Reader Assistant
    """

    async def on_message(self, msg: Message):
        """
        listen for message event
        """
        from_contact: Optional[Contact] = msg.talker()
        text = msg.text()
        print("text::", msg, msg.text())
        room: Optional[Room] = msg.room()
        c = (await room.mentionSelf,)
        print(c, "xxxcontract")
        if text == "ding":
            conversation: Union[Room, Contact] = from_contact if room is None else room
            await conversation.ready()
            await conversation.say("dong")
            file_box = FileBox.from_url(
                "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/" "u=1116676390,2305043183&fm=26&gp=0.jpg",
                name="ding-dong.jpg",
            )
            await conversation.say(file_box)


async def main():
    """Async Main Entry"""
    if "WECHATY_PUPPET_SERVICE_TOKEN" not in os.environ:
        print(
            """
            Error: WECHATY_PUPPET_SERVICE_TOKEN is not found in the environment variables
            You need a TOKEN to run the Python Wechaty. Please goto our README for details
            https://github.com/wechaty/python-wechaty-getting-started/#wechaty_puppet_service_token
        """
        )
    bot = ReaderBot().use(room_invitor)
    await bot.start()


asyncio.run(main())

# Contact <wxid_ytgtw0ktxh4a11> <林攀>@👥 Room <19416436804@chatroom - 小呆tech>]	@ZX涵 >
# https://github.com/wechaty/python-wechaty/blob/0b3ea69f3ecd19d0644cd520947ca8e9092f969a/src/wechaty/user/message.py
