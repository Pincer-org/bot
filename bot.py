import dotenv
import logging
import random
from time import perf_counter

from pincer import Client, command
from pincer.objects import Message, Embed, InteractionFlags
from pincer.objects.embed import EmbedThumbnail, EmbedImage
from pincer.objects.button import ButtonStyle

GUILD_ID = 881531065859190804
logging.basicConfig(level=logging.DEBUG)


def guild_command(**kwargs):
    return command(**kwargs, guild=GUILD)


class Bot(Client):

    def __init__(self) -> None:
        super(Bot, self).__init__(
            token=dotenv.dotenv_values('.env').get("TOKEN")
        )

    @Client.event
    async def on_ready(self) -> None:
        logging.info(f"Logged in as {self.bot} after {perf_counter()} seconds.")

    @guild_command()
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


def main() -> None:
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
