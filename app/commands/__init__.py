from .about import about_command
from .help import help_command
from .ping import ping_command
from .pypi_dl import pypi_dl_command
# from .say import say
# waiting for pincer 0.6.12

commands = (
    about_command,
    help_command,
    ping_command,
    pypi_dl_command,
    # say
)
