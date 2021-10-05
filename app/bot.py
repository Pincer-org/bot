import os
from time import perf_counter

import dotenv
from pincer import Client, command

from .cogs.__init__ import start_config

GUILD_ID = 881531065859190804
TEST_GUILD_ID = 813915317867642910


class Bot(Client):

    def __init__(self):
        self.load_cogs()

        dotenv.load_dotenv('.env')
        super().__init__(token=os.environ.get('TOKEN'))
        self.start_time = perf_counter()

    def load_cogs(self):
        """Load all cogs from the `cogs` directory."""
        for cog_class in start_config:
            self.load_cog(f"app.cogs.{flatten_name(cog_class)}")

    @Client.event
    async def on_ready(self):
        print(
            f"Logged in as {self.bot} "
            f"after {perf_counter() - self.start_time:.3f} seconds."
        )


def flatten_name(cog_name: str) -> str:
    return cog_name.__name__.lower().lower().removesuffix('cog')
