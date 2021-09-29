from pincer.objects import MessageContext, Embed


async def say_command(ctx: MessageContext, message: str):
    return Embed(description=f"{ctx.author.user.mention} said:\n{message}")
