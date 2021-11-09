import logging

from pincer_bot.bot import Bot


logging.basicConfig(level=logging.DEBUG)

bot = Bot()
bot.run()
