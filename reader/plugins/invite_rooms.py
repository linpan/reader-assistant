from typing import Dict

from wechaty_plugin_contrib.contrib import RoomInviterOptions, RoomInviterPlugin
from wechaty_plugin_contrib.matchers import MessageMatcher, RoomMatcher


class RoomInvitePlugin:
    def __init__(self):
        self.rules: Dict[MessageMatcher, RoomMatcher] = {
            MessageMatcher("reader"): RoomMatcher("Room1"),
            MessageMatcher("reading book"): RoomMatcher("Room2"),
        }

    def __call__(self, *args, **kwargs) -> RoomInviterPlugin:
        plugin = RoomInviterPlugin(options=RoomInviterOptions(name="关键字入群插件", rules=self.rules, welcome="欢迎入群"))
        return plugin


room_invitor = RoomInvitePlugin()()
