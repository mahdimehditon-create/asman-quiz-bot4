from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
import os
from handlers import router

TOKEN = os.getenv("API_TOKEN")
WEBHOOK_URL = os.getenv("RENDER_EXTERNAL_URL")

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router)

def main():
    app = web.Application()
    setup_application(app, dp, bot=bot)
    SimpleRequestHandler(bot=bot, dispatcher=dp).register(app)
    web.run_app(app, port=int(os.getenv("PORT", 10000)))

if __name__ == "__main__":
    main()
