import psutil

from pincer.objects import Embed


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
