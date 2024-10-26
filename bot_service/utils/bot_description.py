from aiogram import Bot


async def set_bot_description(bot: Bot):
    description = (
        "Данный бот поможет Вам быстро создавать и рассчитывать накладные, "
        "а также отслеживать посылки"
    )
    await bot.set_my_description(description=description)