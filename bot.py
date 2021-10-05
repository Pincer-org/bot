import logging
import os
from glob import glob
from time import perf_counter

import dotenv
from pincer import Client


class Bot(Client):

    def __init__(self, *args, **kwargs):
        self.load_cogs()

        dotenv.load_dotenv('.env')
        super().__init__(token=os.environ.get('TOKEN'), *args, **kwargs)
        self.start_time = perf_counter()

    def load_cogs(self):
        """Load all cogs from the `cogs` directory."""
        for cog in glob("cogs/*.py"):
            self.load_cog(cog.replace("/", ".").replace("\\", ".")[:-3])
            print("Loaded cogs from", cog)

    @Client.event
    async def on_ready(self):
        print(
            f"Logged in as {self.bot} "
            f"after {perf_counter() - self.start_time:.3f} seconds."
        )


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    Bot().run()
