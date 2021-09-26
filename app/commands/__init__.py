from .about import about_command
from .help import help_command
from .ping import ping_command
from .pypi_dl import pypi_dl_command

commands = (ping_command, about_command, help_command, pypi_dl_command)
