from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client import session
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import  load_dotenv
from aiohttp_socks import ProxyConnector, connector
from handlers.routes import router, notifier


load_dotenv()
TOKEN = getenv("BOT_TOKEN")




dp = Dispatcher()
dp.include_router(router)



async def main():
    connector = ProxyConnector.from_url('socks5://127.0.0.1:22308')
    session = AiohttpSession(proxy='socks5://127.0.0.1:22308')
    bot = Bot(token=TOKEN, session=session)

    asyncio.create_task(notifier(bot))

    print("Start with proxy...")
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())