"""daily plugin"""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any, Callable, List, Optional, Union

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.base import BaseScheduler
from wechaty import Contact, Room, Wechaty, get_logger
from wechaty.plugin import WechatyPlugin, WechatyPluginOptions

log = get_logger("DailyPlugin")


@dataclass
class DailyPluginOptions(WechatyPluginOptions):
    """daily plugin options"""

    room_id: Optional[str] = None
    contact_id: Optional[str] = None
    trigger: Optional[str] = None
    kwargs: Optional[dict] = None
    msg: Optional[str] = None
    name: Optional[str] = None


class DailyPlugin(WechatyPlugin):
    """
    say something everyday, like `Daily Words`
    """

    def __init__(self, options: DailyPluginOptions):
        super().__init__(options)

        # if options.room_id is None and options.contact_id is None:
        #     raise Exception("room_id and contact_id should not all be empty")
        # if options.room_id is not None and options.contact_id is not None:
        #     raise Exception("only one of the room_id contact_id should not " "be none")
        # if options.trigger is None:
        #     raise Exception("trigger should not be none")
        # if options.kwargs is None:
        #     raise Exception("kwargs should not be none")
        # if options.msg is None:
        #     raise Exception("msg should not be none")

        self.options: DailyPluginOptions = options
        self.scheduler: BaseScheduler = AsyncIOScheduler()
        self._scheduler_jobs: List[Any] = []

    @property
    def name(self) -> str:
        """get the name of the plugin"""
        if self.options is None or self.options.name is None:
            return "daily"
        return self.options.name

    async def tick(self, msg) -> None:
        """tick the things"""
        print("mmmmsg::", msg)
        conversation: Union[Room, Contact]
        conversation = self.bot.Room.load("19554643438@chatroom")
        members = await conversation.member_list()
        for m in members:
            owner = self.bot.self().get_id()
            id = m.get_id()
            if owner != id:
                conversation = self.bot.Contact.load(id)
                await conversation.ready()
                await conversation.say("What Up?")
                await asyncio.sleep(3)

    async def init_plugin(self, wechaty: Wechaty) -> None:
        """init plugin"""
        print("init plugin")
        await super().init_plugin(wechaty)
        self.add_interval_job()
        for j in self._scheduler_jobs:
            j(wechaty)
        self.scheduler.start()

    def add_interval_job(self, func: Callable = None) -> None:
        """add interval job"""

        def add_job(bot: Wechaty) -> None:
            self.scheduler.add_job(self.tick, trigger="interval", seconds=45, kwargs={"msg": "我被激活了"})

        self._scheduler_jobs.append(add_job)


class JobPlugin:
    def __call__(self, *args, **kwargs) -> DailyPlugin:
        plugin = DailyPlugin(DailyPluginOptions)
        return plugin


job = JobPlugin()()
