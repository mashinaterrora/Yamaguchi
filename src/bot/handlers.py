from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import re

from src.service.online_sim import check_balance
from src.seleniumAuto.automatization import main


router = Router()

url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Здравствуйте! Введите ссылку на креслице :-)")


@router.message()
async def message_handler(msg: Message):
    text = msg.text
    match = re.search(url_pattern, text)
    if match:
        if not check_balance():
            await msg.answer("На счету недостаточно средств")
        try:
            url = match.group()
            await msg.answer(f"Вы ввели ссылку: {url}, ждите 15-20 секунд и желаем вам приятного массажа :-)")

            script = main(url)
        except:
            await msg.answer("Что-то пошло не так")
    else:
        await msg.answer("То, что вы отправили - не ссылка")