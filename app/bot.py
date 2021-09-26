import os
from time import perf_counter

import dotenv
from pincer import Client, command

from app.commands import commands

GUILD_ID = 881531065859190804


class Bot(Client):

    def __init__(self):
        dotenv.load_dotenv('.env')
        super().__init__(token=os.environ.get('TOKEN'))

        for c, cmd in enumerate(commands):
            command(
                name=cmd.__name__.removesuffix('_command'),
                description=cmd.__doc__ or "Description not set",
                guild=GUILD_ID if not c else None,
            )(cmd)

        self.start_time = perf_counter()

    @Client.event
    async def on_ready(self):
        print(
            f"Logged in as {self.bot} "
            f"after {perf_counter() - self.start_time:.3f} seconds."
        )
