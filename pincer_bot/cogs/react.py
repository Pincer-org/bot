from __future__ import annotations

from random import choice
from pincer import Client
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pincer.objects import UserMessage

PINCER_EMOTES = (
    "pincer_blue:905204976601681921",
    "pincer_green:905204638746279949",
    "pincer_grey:905208040716898305",
    "pincer_orange:905204645989871736",
    "pincer_pink:905204650335162378",
    "pincer_purple:905207327710392330",
    "pincer:881987938303488031",
    "pincer_red:905206299795538032",
    "pincer_cyan:910625755241779261"
)


class React:

    def __init__(self, client: Client) -> None:
        self.client = client

    @Client.event
    async def on_message(self, message: UserMessage):
        if 'pincer' in message.content.lower():
            await message.react(choice(PINCER_EMOTES))


setup = React
