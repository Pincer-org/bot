from pincer import command
from pincer.objects import MessageContext, Embed


@command(description="Say something as the bot!")
async def say(self, ctx: MessageContext, message: str):
    return Embed(description=f"{ctx.author.user.mention} said:\n{message}")
