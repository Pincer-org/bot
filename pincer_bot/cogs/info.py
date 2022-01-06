import re
import requests

from pincer import Client
from pincer import __version__
from pincer.commands import ChatCommandHandler
from pincer.objects import Embed, Message, InteractionFlags, UserMessage
from pincer.utils import TaskScheduler

from pincer_bot.core.command import guild_command
from pincer_bot.tasks.get_pypi_downloads import get_pypi_stats

DL_PATTERN = re.compile(r'downloads: \d*')


class InfoCog:

    def __init__(self, client):
        self.client = client

        task = TaskScheduler(self.client)
        self.get_pypi_downloads = task.loop(minutes=10)(get_pypi_stats)
        self.get_pypi_downloads.start()

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
        height = 15
        pypi = self.client.pypi

        lines = [
            (round((n / pypi.daily_max) * height) * '█').rjust(height, '░')
            for n in self.client.pypi.downloads.values()
        ]

        rotated = '\n'.join(
            ''.join(line)[::-1] for line in zip(*lines)
        )

        return Embed(
            title="PyPI stats",
            description=(
                f"Totals downloads: `{self.client.pypi.total_downloads:,}`\n"
                f"Daily average: `{self.client.pypi.daily_average:,.0f}`"
            )
        ).add_field(
            name="graph",
            value=f'```py\n{rotated}\n```'
        )

    @Client.event
    async def on_message(self, message: UserMessage):
        if "##" not in message.content:
            return

        _, r = message.content.split("##")

        if not (d := r.split('\n')[0]).isdigit():
            return

        url = f"https://github.com/Pincer-org/Pincer/issues/{d}"
        r = requests.get(url)

        if not r.ok:
            return

        content = r.content.split(b'markdown-title">')[1]
        content = content.split(b'</span>')[0]
        content = content.replace(b'<code>', b'`')
        content = content.replace(b'</code>', b'`')

        content = re.sub(
            r'<g-emoji.*alias="(\w+)".*</g-emoji>',
            r':\1:',
            content.decode('utf-8')
        )

        c = await self.client.get_channel(message.channel_id)
        await c.send(Embed(description=f"[{content}]({url})"))


setup = InfoCog
