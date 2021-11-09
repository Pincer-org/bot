from pincer import command
from pincer.utils import Coro

from pincer_bot.constants import GUILD_ID


def guild_command(*args, **kwargs) -> Coro:
    return command(*args, **kwargs, guild=GUILD_ID)
