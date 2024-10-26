import logging
import sys
from os import getenv
from dotenv import load_dotenv
import io

from aiohttp import web
from aiogram import Bot, Dispatcher, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.webhook.aiohttp_server import (SimpleRequestHandler,
                                            setup_application)

from bot_service.keyboards.users.inline import inline_kb_client_menu
from intentions_service.modelVoice import get_intent_by_text, get_intent_by_voice

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
WEB_SERVER_HOST = getenv("WEB_SERVER_HOST")
WEB_SERVER_PORT = int(getenv("WEB_SERVER_PORT"))
WEBHOOK_PATH = getenv("WEBHOOK_PATH")
WEBHOOK_SECRET = getenv("WEBHOOK_SECRET")
BASE_WEBHOOK_URL = getenv("BASE_WEBHOOK_URL")

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    text, reply_markup = inline_kb_client_menu()
    await message.answer(text=text, reply_markup=reply_markup)


@router.message(F.voice)
async def voice_message_handler(message: Message, bot: Bot) -> None:
    voice = message.voice
    voice_file_info = await bot.get_file(voice.file_id)
    # voice_ogg = io.BytesIO()
    await bot.download_file(voice_file_info.file_path, f"intentions_service/voices/{voice_file_info.file_unique_id}.ogg")
    intent = get_intent_by_voice(f"{voice_file_info.file_unique_id}")
    await message.answer(intent)
    # voice_mp3_path = f"voice-{voice.file_unique_id}.wav"
    # AudioSegment.from_file(voice_ogg, format="ogg").export(
    #     voice_mp3_path, format="wav"
    # )


@router.message(F.text)
async def echo_handler(message: Message) -> None:
    intent = get_intent_by_text(message.text)
    #intent = message.text
    await message.answer(text=intent)


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}",
                          secret_token=WEBHOOK_SECRET)


def main() -> None:
    logging.info("Starting bot")
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(on_startup)
    bot = Bot(token=TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )

    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    setup_application(app, dp, bot=bot)

    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
