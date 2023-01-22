from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.JobButton import button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("<b> Эълон бериш учун керакли бўлимни танланг! </b>", reply_markup=button, parse_mode="HTML")
