import logging
import re
from time import perf_counter

import dotenv
import requests
from pincer import Client, command
from pincer.commands import ChatCommandHandler
from pincer.objects import Embed, Message, InteractionFlags

GUILD_ID = 881531065859190804
logging.basicConfig(level=logging.DEBUG)

dl_pattern = re.compile(r'downloads: \d*')

pypi_download_url = (
    "https://img.shields.io/badge/dynamic/json?"
    "label=downloads&query=%24.total_downloads"
    "&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2FPincer"
)


class Bot(Client):

    def __init__(self) -> None:
        super(Bot, self).__init__(
            token=dotenv.dotenv_values('.env').get("TOKEN")
        )

    @Client.event
    async def on_ready(self) -> None:
        logging.info(f"Logged in as {self.bot} after {perf_counter()} seconds.")

    @command(guild=GUILD_ID, description="Embed example command")
    async def about(self) -> Embed:
        return Embed(
            title="Pincer - 0.6.4",
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

    @command(description="Number of PyPI downloads")
    async def pypi_dl(self):
        res = requests.get(pypi_download_url)
        downloads = re.findall(dl_pattern, res.content.decode())[0]
        amount = downloads.split(' ')[1]
        return f"> `{amount}` *Updates every days*"

    @command(description="An help command")
    async def help(self):
        return Message(
            content='>>> ' + '\n'.join(
                f"`{cmd_name.capitalize()}` - {cmd_obj.app.description}"
                for cmd_name, cmd_obj in ChatCommandHandler.register.items()
            ),
            flags=InteractionFlags.EPHEMERAL
        )


def main() -> None:
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
