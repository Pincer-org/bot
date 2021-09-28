import os
from time import perf_counter

import dotenv
from pincer import Client, command

from app.commands import commands

GUILD_ID = 881531065859190804
TEST_GUILD_ID = 813915317867642910


class Bot(Client):

    def __init__(self):
        for cmd in commands:
            command_name = cmd.__name__.lower()
            if command_name.endswith('_command'):
                command_name = command_name[:-8]

            self.__setattr__(
                command_name,
                command(
                    name=command_name,
                    description=cmd.__doc__ or "Description not set",
                    guild=TEST_GUILD_ID
                )(cmd)
            )

        dotenv.load_dotenv('.env')
        super().__init__(token=os.environ.get('TOKEN'))
        self.start_time = perf_counter()

    @Client.event
    async def on_ready(self):
        print(
            f"Logged in as {self.bot} "
            f"after {perf_counter() - self.start_time:.3f} seconds."
        )
