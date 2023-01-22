from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button = ReplyKeyboardMarkup(resize_keyboard=True,
                             keyboard=[
                                 [KeyboardButton(text="🏡 Уй-жой Бозори"),
                                  ],
                             ])



checkbtn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
                               keyboard=[
                                   [KeyboardButton(text="✅ Эълонни жойлаш"),
                                    KeyboardButton(text="❌ Эълонни қайтадан ёзиш")],

                               ])


newbutton = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [KeyboardButton(text="🛑 Bekor qilish")]
                                ])


otkazishButton = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [KeyboardButton(text="⏭️ Кейингиси")],
                                ])

homeTypes = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
                                keyboard=[
                                    [KeyboardButton(text="Квартира"), KeyboardButton(text="Ҳовли Участка")],
                                    [KeyboardButton(text="Қуруқ Ер"), KeyboardButton(text="Дача")],
                                    [KeyboardButton(text="⬅️ Ортга")],
                                ])






