from __future__ import annotations

from pincer import Client
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pincer.objects import UserMessage


class React:

    def __init__(self, client: Client) -> None:
        self.client = client

    @staticmethod
    async def create_reaction(message: UserMessage, reaction: str):
        await message._http.put(
            f"/channels/{message.channel_id}/messages/{message.id}/reactions/"
            f"{reaction}/@me",
            None
        )

    @Client.event
    async def on_message(self, message: UserMessage):
        if 'pincer' in message.content:
            await self.create_reaction(message, "🚀")


setup = React
