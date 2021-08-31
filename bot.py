from time import perf_counter

import dotenv
import logging

from pincer.client import Client

logging.basicConfig(level=logging.DEBUG)


class Bot(Client):

    def __init__(self) -> None:
        super(Bot, self).__init__(
            token=dotenv.dotenv_values('.env').get("TOKEN")
        )

    @Client.event
    async def on_ready(self) -> None:
        logging.info(f"Logged in as {self.bot} after {perf_counter()} seconds.")


def main() -> None:
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
