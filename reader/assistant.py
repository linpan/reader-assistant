"""
"""
import asyncio
import os
from typing import Optional, Union

from wechaty import Contact, Room, Wechaty
from wechaty.user import Message

from reader.plugins.invite_rooms import room_invitor
from reader.plugins.speech_to_text import speech

os.environ["WECHATY_PUPPET_SERVICE_TOKEN"] = "puppet_paimon_72a5c28b-8ddf-4900-a42e-25518aa3cd76"

bot: Optional[Wechaty] = None


class ReaderBot(Wechaty):
    """
    Reader Assistant
    """

    # master
    owner = None

    async def on_login(self, contact: Contact) -> None:
        pass

    async def on_message(self, msg: Message):
        """
        listen for message event
        """
        pass


async def main():
    """Async Main EntryPoint"""
    if "WECHATY_PUPPET_SERVICE_TOKEN" not in os.environ:
        raise EnvironmentError(
            """
            Error: WECHATY_PUPPET_SERVICE_TOKEN is not found in the environment variables
            """
        )
    global bot
    reader = ReaderBot().use([speech, room_invitor])
    await reader.start()


asyncio.run(main())
