import re

from pincer.commands import command
from pincer.objects import Embed, MessageContext

DL_PATTERN = re.compile(r'downloads: \d*')
PYPI_DOWNLOAD_URL = (
    "https://img.shields.io/badge/dynamic/json?"
    "label=downloads&query=%24.total_downloads"
    "&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2FPincer"
)


class FunCog:

    @command(name="say")
    async def say_command(self, ctx: MessageContext, message: str):
        return Embed(description=f"{ctx.author.user.mention} said:\n{message}")

    @command(name="ping")
    async def ping_command(self) -> str:
        return 'pong'


setup = FunCog
