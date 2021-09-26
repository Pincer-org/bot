from pincer.commands import ChatCommandHandler
from pincer.objects import Message, InteractionFlags


async def help_command():
    return Message(
        content='>>> ' + '\n'.join(
            f"`{cmd_name.capitalize()}` - {cmd_obj.app.description}"
            for cmd_name, cmd_obj in ChatCommandHandler.register.items()
        ),
        flags=InteractionFlags.EPHEMERAL
    )