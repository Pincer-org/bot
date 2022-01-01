from pincer.objects import Embed, MessageContext

from pincer_bot.core.command import guild_command


class FunCog:

    @guild_command(name="say")
    async def say_command(self, ctx: MessageContext, message: str):
        return Embed(description=f"{ctx.author.mention} said:\n{message}")

    @guild_command(name="ping")
    async def ping_command(self) -> str:
        return 'pong'


setup = FunCog
