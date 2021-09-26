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
            self.__setattr__(
                cmd.__name__,
                command(
                    name=cmd.__name__,
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
