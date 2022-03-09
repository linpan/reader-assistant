import re
from typing import Union

import pilk
from wechaty import Contact, FileBox, Message, MessageType, Room, Wechaty, get_logger
from wechaty.plugin import WechatyPlugin

from reader import client

logger = get_logger(__name__)


def get_file_content(path):
    with open(path, "rb") as fp:
        return fp.read()


class SpeechTextPlugin(WechatyPlugin):
    """chat history plugin"""

    @property
    def name(self) -> str:
        return "speech"

    async def init_plugin(self, wechaty: Wechaty) -> None:
        await super().init_plugin(wechaty)

    async def on_message(self, msg: Message) -> None:
        from_contact = msg.talker()
        text = msg.text()
        if msg.type() == MessageType.MESSAGE_TYPE_AUDIO:
            audio_file = await msg.to_file_box()
            file_name = audio_file.name
            await audio_file.to_file()
            newfile = "test2.pcm"
            pilk.decode(file_name, newfile)
            data = client.asr(
                get_file_content(newfile),
                "pcm",
                16000,
                {
                    "dev_pid": 1537,
                },
            )
            if data["err_msg"] == "success.":
                await from_contact.say(data["result"][0])


class SpeechPlugin:
    def __call__(self, *args, **kwargs) -> SpeechTextPlugin:
        plugin = SpeechTextPlugin()
        return plugin


speech = SpeechPlugin()()
