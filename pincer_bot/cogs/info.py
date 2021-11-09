import re

import requests
from pincer import __version__
from pincer.commands import ChatCommandHandler, command
from pincer.objects import Embed, Message, InteractionFlags

from pincer_bot.core.command import guild_command

DL_PATTERN = re.compile(r'downloads: \d*')
PYPI_DOWNLOAD_URL = (
    "https://img.shields.io/badge/dynamic/json?"
    "label=downloads&query=%24.total_downloads"
    "&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2FPincer"
)


class InfoCog:

    @guild_command(name='about')
    async def about_command(self) -> Embed:
        return Embed(
            title=f"Pincer - {__version__}",
            description=(
                "🚀 An asynchronous python API wrapper meant to replace "
                "discord.py\n> Snappy discord api wrapper written "
                "with aiohttp & websockets"
            )
        ).add_field(
            name="**Github Repository**",
            value="> https://github.com/Pincer-org/Pincer"
        ).add_field(
            name="Website",
            value="> https://pincer.dev"
        ).add_field(
            name="PyPI package",
            value="> https://pypi.org/project/Pincer"
        ).add_field(
            name="ReadTheDocs",
            value="> https://pincer.readthedocs.io"
        ).set_footer(
            text="The package is currently within the planning phase",
            icon_url="https://pincer.dev/img/icon.png"
        ).set_author(
            name="Pincer",
            url='https://pincer.dev',
            icon_url="https://pincer.dev/img/icon.png"
        ).set_thumbnail(
            url="https://pincer.dev/img/icon.png"
        ).set_image(
            url=(
                "https://repository-images.githubusercontent.com"
                "/400871418/045ebf39-7c6e-4c3a-b744-0c3122374203"
            )
        )

    @guild_command(name="help")
    async def help_command(self):
        return Message(
            content='>>> ' + '\n'.join(
                f"`{cmd_name.capitalize()}` - {cmd_obj.app.description}"
                for cmd_name, cmd_obj in ChatCommandHandler.register.items()
            ),
            flags=InteractionFlags.EPHEMERAL
        )

    @guild_command(name="pypi_dl")
    async def pypi_dl_command(self):
        res = requests.get(PYPI_DOWNLOAD_URL)
        downloads = re.findall(DL_PATTERN, res.content.decode())[0]
        amount = downloads.split(' ')[1]
        return f"> `{amount}` *Updates every days*"


setup = InfoCog
