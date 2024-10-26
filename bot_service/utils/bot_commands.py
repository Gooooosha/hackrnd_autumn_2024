from aiogram import Bot
from aiogram.types import (
    BotCommand,
    BotCommandScopeAllPrivateChats,
)


async def set_commands(
    bot: Bot,
) -> None:
    commands = [BotCommand(command="menu", description="Перейти в главное меню")]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())