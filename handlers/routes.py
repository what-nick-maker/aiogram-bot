import asyncio

from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

router = Router()


subscribers = set()

async def notifier(bot: Bot):
    while True:
        if subscribers:
            for user_id in list(subscribers):
                try:
                    await bot.send_message(user_id, "Your standart message")
                except Exception:
                    pass
        await asyncio.sleep(10)

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Hello!\n"
        "I can help with notifications!\n\n"
        "Commands:\n"
        "/subscribe - subscribe to notification\n"
        "/unsubscribe - unsubscribe to notification\n"
        "/subscribers - list of subscribers"
    )

@router.message(Command("subscribe"))
async def subscribe(message: Message):
    user_id = message.from_user.id

    subscribers.add(user_id)

    await message.answer("You were subscribed to notifications!")

@router.message(Command("unsubscribe"))
async def unsubscribe(message: Message):
    user_id = message.from_user.id

    subscribers.remove(user_id)

    await message.answer("You were unsubscribed to notifications!")


@router.message(Command("subscribers"))
async def subscribers_cmd(message: Message):
    if not subscribers:
        await message.answer("No one")
        return

    text = "Subscribers:\n"
    for uid in subscribers:
        text += f"- {uid}\n"
    await message.answer(text)