import re
import psutil
import requests
from pincer import __version__
from pincer.commands import ChatCommandHandler
from pincer.objects import Embed, Message, InteractionFlags, MessageContext

DL_PATTERN = re.compile(r'downloads: \d*')
PYPI_DOWNLOAD_URL = (
    "https://img.shields.io/badge/dynamic/json?"
    "label=downloads&query=%24.total_downloads"
    "&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2FPincer"
)


class InfoCog:
    ...

    @staticmethod
    async def about_command() -> Embed:
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

    @staticmethod
    async def help_command():
        return Message(
            content='>>> ' + '\n'.join(
                f"`{cmd_name.capitalize()}` - {cmd_obj.app.description}"
                for cmd_name, cmd_obj in ChatCommandHandler.register.items()
            ),
            flags=InteractionFlags.EPHEMERAL
        )

    @staticmethod
    async def panel_command() -> Embed:
        """Panel status command."""
        mb: int = 1024 ** 2

        vm = psutil.virtual_memory()
        cpu_freq = psutil.cpu_freq()
        cpu_percent = psutil.cpu_percent()
        disk = psutil.disk_usage('.')

        stats = {
            'ram': (
                100 * (vm.used / vm.total),
                f'{(vm.total / mb) / 1000:,.3f}',
                'Gb'
            ),
            'cpu': (
                cpu_percent,
                f"{cpu_freq.current / 1000:.1f}`/`{cpu_freq.max / 1000:.1f}",
                'Ghz'
            ),
            'disk': (
                100 * (disk.used / disk.total),
                f'{disk.total / mb:,.0f}', 'Mb'
            )
        }

        return Embed(
            title="Panel Stats",
            description="The bot is hosted on a private vps."
        ).add_fields(
            stats.items(),
            map_title=lambda name: name.upper(),
            map_values=lambda percent, info, unit: (
                f"> `{percent:.3f}` **%**\n- `{info}` **{unit}**"
            )
        )

    @staticmethod
    async def ping_command() -> str:
        return 'pong'

    @staticmethod
    async def pypi_dl_command():
        res = requests.get(PYPI_DOWNLOAD_URL)
        downloads = re.findall(DL_PATTERN, res.content.decode())[0]
        amount = downloads.split(' ')[1]
        return f"> `{amount}` *Updates every days*"

    @staticmethod
    async def say_command(ctx: MessageContext, message: str):
        return Embed(description=f"{ctx.author.user.mention} said:\n{message}")


setup = InfoCog
