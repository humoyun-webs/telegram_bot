import logging
from typing import List

from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ContentType
from loader import dp, bot
from aiogram.types import ReplyKeyboardRemove
from api import create_worker
from keyboards.default.JobButton import checkbtn, button, homeTypes
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher.filters import Text, state
from keyboards.default.JobButton import newbutton, otkazishButton
from states.HomeKravtiraState import HomeKvartira
from config import *
from check_user import check_user, get_check_button
from transliterate import to_cyrillic
from keyboards.inline.HomeButton import regions, homeType, remontButton, jihozlarButton, valyutaButton

from aiogram.dispatcher.dispatcher import FSMContext
from aiogram.types import ChatMember, ChatPhoto
from aiogram.bot.bot import types

mode = "Markdown"


@dp.message_handler(Text(startswith="🏡 Уй-жой"))
async def first(message: types.Message):
    get_chat = await bot.get_chat_member(iddd, message.chat.id)

    if check_user(get_chat):
        await message.answer("<b> Уй-жой турини танланг! </b>", reply_markup=homeTypes, parse_mode="HTML")
    else:
        await bot.send_message(message.chat.id,
                               "*Аввал ушбу каналга обуна бўлинг ва 'тасдиқлаш' тугмасини босинг*",
                               parse_mode=mode, reply_markup=get_check_button())


@dp.callback_query_handler(text="check_user", chat_type="private")
async def checkMember(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(iddd, call.message.chat.id)

    if check_user(get_chat):
        await call.message.answer("Уй-жой турини танланг!", reply_markup=homeTypes)
    else:
        await call.answer("Каналга обуна бўлмадингиз❗", show_alert=True)


@dp.message_handler(text="⬅️ Ортга")
async def ortga(message: types.Message):
    await message.answer("<b> Эълон бериш учун керакли бўлимни танланг! </b>", reply_markup=button, parse_mode="HTML")




