import logging
from typing import List

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
from keyboards.inline.HomeButton import regions, homeType, remontButton, jihozlarButton, valyutaButton, borYoq

from aiogram.dispatcher.dispatcher import FSMContext
from aiogram.types import ChatMember, ChatPhoto
from aiogram.bot.bot import types

mode = "Markdown"


@dp.message_handler(Text(startswith="Квартира"), state=None)
async def first(message: types.Message):
    await message.answer("Ҳудудни танланг: ", reply_markup=regions)
    await HomeKvartira.region.set()


@dp.callback_query_handler(text='toshkent_shahar', chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Тошкент  #Шаҳар"
    await callback_query.answer("Pressed")
    await state.update_data({
        "region": text
    })
    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг: ")

    await HomeKvartira.next()


@dp.callback_query_handler(text='Toshkent viloyati', chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Тошкент  #Вилояти"
    await callback_query.answer("Pressed")
    await state.update_data({
        "region": text
    })
    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг: ")
    await HomeKvartira.next()


@dp.callback_query_handler(text='Andijon', chat_type="private", state=HomeKvartira.region)
async def andijon(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Andijon  #Viloyati"
    await callback_query.answer("Pressed")
    await state.update_data({
        "region": text
    })
    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг: ")

    await HomeKvartira.next()


@dp.callback_query_handler(text='Namangan', chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Наманган  #Вилояти"
    await callback_query.answer("Pressed")
    await state.update_data({
        "region": text
    })
    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг: ")
    await HomeKvartira.next()


@dp.callback_query_handler(text="Farg'ona", chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Фарғона  #Вилояти"
    await callback_query.answer("Pressed")
    await state.update_data({
        "region": text
    })
    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг: ")
    await HomeKvartira.next()


@dp.callback_query_handler(text='Samarqand', chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Самарқанд  #Вилояти"
    await callback_query.answer("Pressed")

    await state.update_data({
        "region": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг: ")
    await HomeKvartira.next()


@dp.callback_query_handler(text='Buxoro', chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Бухоро  #Вилояти"
    await callback_query.answer("Pressed")

    await state.update_data({
        "region": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг: ")
    await HomeKvartira.next()


@dp.callback_query_handler(text="Sirdaryo", chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Сирдарё  #Вилояти"
    await callback_query.answer("Pressed")

    await state.update_data({
        "region": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг: ")
    await HomeKvartira.next()


@dp.callback_query_handler(text="Qashqadaryo", chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Қашқадарё  #Вилояти"
    await callback_query.answer("Pressed")

    await state.update_data({
        "region": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг: ")
    await HomeKvartira.next()


@dp.callback_query_handler(text="Surxandaryo", chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Сурхандарё  #Вилояти"
    await callback_query.answer("Pressed")

    await state.update_data({
        "region": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг: ")
    await HomeKvartira.next()


@dp.callback_query_handler(text="Navoiy", chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Навоий  #Вилояти"
    await callback_query.answer("Pressed")

    await state.update_data({
        "region": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг:  ")
    await HomeKvartira.next()


@dp.callback_query_handler(text="Jizzax", chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Жиззах  #Вилояти"
    await callback_query.answer("Pressed")

    await state.update_data({
        "region": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг: ")
    await HomeKvartira.next()


@dp.callback_query_handler(text="Xorazm", chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Хоразм  #Вилояти"
    await callback_query.answer("Pressed")

    await state.update_data({
        "region": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг:  ")
    await HomeKvartira.next()


@dp.callback_query_handler(text="Qoraqalpog'iston", chat_type="private", state=HomeKvartira.region)
async def tashkent(callback_query: types.CallbackQuery, state: FSMContext):
    text = "#Қорақалпоғистон"
    await callback_query.answer("Pressed")

    await state.update_data({
        "region": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Умумий майдонини ёзинг: ")
    await HomeKvartira.next()


# @dp.message_handler(lambda message: not message.text.isdigit(), state=HomeKvartira.umumiyMaydon)
# async def check_umumiy(message: types.Message):
#     await message.reply("❗ Умумий майдонни фақатгина сон қийматида киритинг")


@dp.message_handler(state=HomeKvartira.umumiyMaydon)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "umumiyMaydon": text
    })
    await message.answer(text="Хоналар сонини ёзинг: ")

    await HomeKvartira.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=HomeKvartira.xonalar)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=HomeKvartira.xonalar)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data({
        "xonalar": text
    })
    await message.answer(text="Нечанчи қаватда жойлашган? ")

    await HomeKvartira.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=HomeKvartira.qavat)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=HomeKvartira.qavat)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qavat": text
    })
    await message.answer(text="Неча қаватлик бино? ")

    await HomeKvartira.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=HomeKvartira.qavatlik)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=HomeKvartira.qavatlik)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data({
        "qavatlik": text
    })
    await message.answer(text="Ремонти қандай? ", reply_markup=remontButton)
    await HomeKvartira.next()


# remont start ========================================================

@dp.callback_query_handler(text='Evroremont', state=HomeKvartira.remont, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Евроремонт"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await HomeKvartira.next()


@dp.callback_query_handler(text="Ta'mirlangan", state=HomeKvartira.remont, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Таъмирланган"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await HomeKvartira.next()


@dp.callback_query_handler(text="O'rtacha", state=HomeKvartira.remont, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Ўртача"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await HomeKvartira.next()


@dp.callback_query_handler(text="Ta'mirsiz", state=HomeKvartira.remont, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Таъмирсиз"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await HomeKvartira.next()


# remont finish ========================================================


# jihoz start ===============================================

@dp.callback_query_handler(text='Mavjud', state=HomeKvartira.jihozlar, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "бор"
    await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="🔥 Газ борми?",
                           reply_markup=borYoq)
    await HomeKvartira.next()


@dp.callback_query_handler(text='Jihozlarsiz', state=HomeKvartira.jihozlar, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "йўқ"
    await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="🔥 Газ борми?",
                           reply_markup=borYoq)
    await HomeKvartira.next()


# jihoz finish ===============================================

# ========================= komunal start =========================
@dp.callback_query_handler(text="bor", state=HomeKvartira.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Газ ✅"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💡 Свет борми?", reply_markup=borYoq)
    await HomeKvartira.next()


@dp.callback_query_handler(text="yoq", state=HomeKvartira.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Mavjud emas"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💡 Свет борми?", reply_markup=borYoq)
    await HomeKvartira.next()

    # ========================================================================


@dp.callback_query_handler(text="bor", state=HomeKvartira.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Свет ✅"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💦 Сув борми?", reply_markup=borYoq)
    await HomeKvartira.next()


@dp.callback_query_handler(text="yoq", state=HomeKvartira.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Mavjud emas"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💦 Сув борми?", reply_markup=borYoq)
    await HomeKvartira.next()


# ============================================================================

@dp.callback_query_handler(text="bor", state=HomeKvartira.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Сув ✅"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Канализация борми?",
                           reply_markup=borYoq)
    await HomeKvartira.next()


@dp.callback_query_handler(text="yoq", state=HomeKvartira.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Mavjud emas"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Канализация борми?",
                           reply_markup=borYoq)
    await HomeKvartira.next()


# ========================================================================
@dp.callback_query_handler(text="bor", state=HomeKvartira.kanalizatsiya)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Канализация ✅"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "kanalizatsiya": text
    })

    await callback_query.message.answer(
        text="Қўшимча маълумотингиз бўлса,  ёзишингиз мумкин.  \n\n Йўқ бўлса 'Кейингиси' тугмасини босинг",
        reply_markup=otkazishButton)

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await HomeKvartira.next()
    else:
        await HomeKvartira.next()


@dp.callback_query_handler(text="yoq", state=HomeKvartira.kanalizatsiya)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Mavjud emas"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "kanalizatsiya": text
    })

    await callback_query.message.answer(
        text="Қўшимча маълумотингиз бўлса,  ёзишингиз мумкин.  \n\n Йўқ бўлса 'Кейингиси' тугмасини босинг",
        reply_markup=otkazishButton)

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await HomeKvartira.next()
    else:
        await HomeKvartira.next()


@dp.message_handler(state=HomeKvartira.qoshimchaMalumot)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qoshimchaMalumot": text
    })
    await message.answer(text="Қайси валютада нарх белгиламоқчисиз?",
                         reply_markup=valyutaButton)

    await HomeKvartira.next()


# Price ==============


@dp.callback_query_handler(text='USD', state=HomeKvartira.valyuta, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = " $"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Нархини ёзинг: ")

    await HomeKvartira.next()


@dp.callback_query_handler(text='SUM', state=HomeKvartira.valyuta, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = " сўм"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Нархини ёзинг: ")

    await HomeKvartira.next()


# Price ==============


# @dp.message_handler(lambda message: not message.text.isdigit(), state=HomeKvartira.narxi)
# async def check_umumiy(message: types.Message):
#     await message.reply("❗ Нархни фақатгина сон қийматида киритинг")


@dp.message_handler(state=HomeKvartira.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "narxi": text
    })
    await message.answer(text="Манзилни ёзинг: ")

    await HomeKvartira.next()


@dp.message_handler(state=HomeKvartira.manzil)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "manzil": text
    })
    await message.answer(text="Мўлжални ёзинг: ")

    await HomeKvartira.next()


@dp.message_handler(state=HomeKvartira.moljal)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "moljal": text
    })
    await message.answer(text="Телефон рақамини ёзинг: ")

    await HomeKvartira.next()


# @dp.message_handler(lambda message: not message.text.isdigit(), state=HomeKvartira.telNumberOne)
# async def check_umumiy(message: types.Message):
#     await message.reply("❗ Телефон рақамни фақатгина сон қийматида киритинг")


@dp.message_handler(state=HomeKvartira.telNumberOne)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    telNumber = message.text

    await state.update_data({
        "telNumberOne": telNumber
    })

    await message.answer(text="Зарур бўлса 2-рақамни киритинг,  \n\n  ёки 'Кейингиси'  тугмасини босинг",
                         reply_markup=otkazishButton)
    if message.text == "⏭️ Кейингиси":
        await state.update_data({
            "telNumberTwo": ""
        })
        await HomeKvartira.next()
    else:
        await HomeKvartira.next()


@dp.message_handler(state=HomeKvartira.telNumberTwo)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "telNumberTwo": text
    })
    await message.answer(text="Расмларни жойлаш (10 - тагача)")

    await HomeKvartira.next()


@dp.message_handler(is_media_group=True, state=HomeKvartira.images, content_types=types.ContentTypes.PHOTO)
async def images(message: types.Message, album: List[types.Message], state: FSMContext):
    chat_id = message.chat.id
    media_group = types.MediaGroup()

    for obj in album:
        if obj.content_type == 'photo':
            if obj.photo:
                file_id = obj.photo[-1].file_id
            else:
                file_id = obj[obj.content_type].file_id
            try:
                media_group.attach({"media": file_id,
                                    "type": obj.content_type,
                                    "caption": obj.caption})

            except Exception as err:
                logging.exception(err)
                return await message.answer("Бундай файл юклаб бўлмайди")
        else:
            await message.reply("❗ Расмдан бошқа файл турини юклай олмайсиз")

    await state.update_data({
        'images': media_group
    })

    data = await state.get_data()

    # ==============================================================================================================
    # ==============================================================================================================

    if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
        if data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
            'kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + "Йўқ" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15
            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15
            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['suv'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15
            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['svet'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['suv'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['svet'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['suv'] + ", " + data['svet'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['svet'] + ", " + data['suv'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        else:
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
    # ============================================================================================
    # ============================================================================================

    elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
        if data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
            'kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + "Йўқ" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data16
            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16
            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['suv'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16
            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['svet'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['suv'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['svet'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['suv'] + ", " + data['svet'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['svet'] + ", " + data['suv'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        else:
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
    # ================================================================================================
    # ================================================================================================

    elif data['telNumberTwo'] == "⏭️ Кейингиси":
        if data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
            'kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + "Йўқ" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15
            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['kanalizatsiya'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15
            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['suv'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15
            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['svet'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['suv'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['svet'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['suv'] + ", " + data['svet'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['svet'] + ", " + data['suv'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        else:
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
    # =============================================================================================
    # =============================================================================================
    else:
        if data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
            'kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + "Йўқ" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16
            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16
            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['suv'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16
            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['svet'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['suv'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['svet'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['suv'] + ", " + data['svet'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['gaz'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['svet'] + ", " + data['suv'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['svet'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['suv'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        elif data['kanalizatsiya'] == "Mavjud emas":
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()
        else:
            data1 = data['region'] + "\n"
            data2 = "#Квартира  #Сотилади \n\n"
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + ", " + data[
                'kanalizatsiya'] + " бор" + "\n"
            data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data12 = "📌 Манзил: " + data['manzil'] + "\n"
            data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n"

            result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

            cyrillic_text = to_cyrillic(result)

            await bot.send_media_group(chat_id=chat_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
            await bot.send_message(chat_id=chat_id,
                                   text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
            await HomeKvartira.next()


# ==================================================================================================
# ==================================================================================================
# ==================================================================================================
# ==================================================================================================
# ==================================================================================================

@dp.message_handler(state=HomeKvartira.check)
async def check(message: types.Message, state: FSMContext):
    mycheck = message.text
    chat_id = message.chat.id

    if mycheck == "✅ Эълонни жойлаш":
        data = await state.get_data()
        media_group = data['images']

        if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
            if data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + "Йўқ" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['suv'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15
                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['svet'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['suv'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['svet'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['suv'] + ", " + data['svet'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['svet'] + ", " + data['suv'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            else:
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()


        elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
            if data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + "Йўқ" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['suv'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['svet'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['suv'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['svet'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['suv'] + ", " + data['svet'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['svet'] + ", " + data['suv'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            else:
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()

        elif data['telNumberTwo'] == "⏭️ Кейингиси":
            if data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + "Йўқ" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['kanalizatsiya'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['suv'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['svet'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['suv'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['svet'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['suv'] + ", " + data['svet'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['svet'] + ", " + data['suv'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            else:
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
        else:
            if data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + "Йўқ" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['suv'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                
                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['svet'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas" and data[
                'kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['svet'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['suv'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['svet'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['suv'] + ", " + data['svet'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas" and data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['suv'] == "Mavjud emas" and data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['gaz'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['svet'] + ", " + data['suv'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['svet'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['suv'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['suv'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            elif data['kanalizatsiya'] == "Mavjud emas":
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
            else:
                data1 = data['region'] + "\n"
                data2 = "#Квартира  #Сотилади \n\n"
                data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
                data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
                data5 = "🔷 Қавати: " + data['qavat'] + "-қават" + "\n"
                data6 = "🔷 Неча қаватли: " + data['qavatlik'] + "\n"
                data7 = "🔷 Ремонти: " + data['remont'] + "\n"
                data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
                data9 = "🔷 " + data['gaz'] + ", " + data['svet'] + ", " + data['suv'] + ", " + data[
                    'kanalizatsiya'] + " бор" + "\n"
                data11 = "🔷 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
                data12 = "📌 Манзил: " + data['manzil'] + "\n"
                data13 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
                data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
                data10 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n"
                data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"
                data20 = "<a href='https://t.me/demo_bot_2022Bot'><b>        ЭЪЛОН БЕРИШ</b></a>\n\n"

                result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data15 + data16

                crillic_text = to_cyrillic(result) + data20
                await bot.send_media_group(chat_id=-1001749531048, media=media_group)
                await bot.send_message(chat_id=-1001749531048, text=crillic_text, parse_mode="HTML")
                await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=button)
                await state.finish()
    else:
        await bot.send_message(chat_id=chat_id, text="❌ Эълон қабул қилинмади")
        await bot.send_message(chat_id=chat_id, text="Еълон бериш учун қайтадан уриниб кўринг", reply_markup=button)
        await state.finish()
