import logging

from pincer import Intents
from pincer_bot.bot import Bot


logging.basicConfig(level=logging.DEBUG)

bot = Bot(intents=Intents.all())
bot.run()
