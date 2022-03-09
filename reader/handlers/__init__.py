import asyncio
from typing import List

from wechaty import Contact, Room, Wechaty
from wechaty_puppet import ContactType
from wechaty_puppet.logger import get_logger

MAX_CONTACTS = 10
INTERVAL = 3

log = get_logger("ContactBot")


async def handle_login(bot, user: Contact) -> None:
    """Handle the login event"""

    log.info("%s logged in", user.name)
    log.info("%s logged in", user.contact_id)


async def find_rooms(bot: Wechaty) -> List[Room]:
    """find the matched rooms"""
    print("11111")
    room = await bot.Room.find({"topic": "KEG-赛尔"})
    print(room)
    print("eeeee")
