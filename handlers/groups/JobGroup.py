import io
from keyboards.default.JobButton import button
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command,CallbackQuery

from filters import IsGroup,IsGroupCall
from filters.admins import AdminFilter
from aiogram.dispatcher.filters import Text
from loader import dp, bot
from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
@dp.callback_query_handler(IsGroupCall(),Text(startswith='send'))
async def send(call:CallbackQuery):

    await call.answer(cache_time=60)
    id = call.message.message_id
    text = call.message.text
    await bot.send_message(chat_id=env.int('CHANNEL'), text=text)
    await call.message.delete()
    data = call.data
    await bot.send_message(chat_id=data[4:],
                           text="✅ E'lon kanalga joylandi!",
                           reply_markup=button)

    await call.message.answer("✅ Hurmatli admin xabar yuborildi!")

@dp.callback_query_handler(IsGroupCall(), Text(startswith='cancel'))
async def send(call:CallbackQuery):
    await call.message.delete()
    id = call.message.message_id
    data = call.data


    await bot.send_message(chat_id=data[6:],
                           text="😕 Uzr xabardagi xatoliklar sabab e'lon kanalga chiqarilmadi!\nIltimos qaytadan ma'lumotlarni kiriting!",
                           reply_markup=button)
    await call.message.answer("🗑 E'lon o'chirildi!")

