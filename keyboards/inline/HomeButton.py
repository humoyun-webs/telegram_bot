from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


regions = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                inline_keyboard=[
                                    [InlineKeyboardButton(text="Тошкент шаҳар", callback_data="toshkent_shahar"), InlineKeyboardButton(text="Тошкент вилояти", callback_data="Toshkent viloyati")],
                                    [InlineKeyboardButton(text="Андижон", callback_data="Andijon"), InlineKeyboardButton(text="Наманган", callback_data="Namangan")],

                                    [InlineKeyboardButton(text="Фарғона", callback_data="Farg'ona"), InlineKeyboardButton(text="Самарқанд", callback_data="Samarqand")],

                                    [InlineKeyboardButton(text="Бухоро", callback_data="Buxoro"), InlineKeyboardButton(text="Сирдарё", callback_data="Sirdaryo")],

                                    [InlineKeyboardButton(text="Қашқадарё", callback_data="Qashqadaryo"), InlineKeyboardButton(text="Сурхoндарё", callback_data="Surxandaryo")],

                                    [InlineKeyboardButton(text="Навоий", callback_data="Navoiy"), InlineKeyboardButton(text="Жиззах", callback_data="Jizzax")],

                                    [InlineKeyboardButton(text="Хоразм", callback_data="Xorazm"), InlineKeyboardButton(text="Қорақалпоғистон", callback_data="Qoraqalpog'iston")],

                                ])

homeType = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                inline_keyboard=[
                                    [InlineKeyboardButton(text="Квартира", callback_data="Kvartira"),
                                     InlineKeyboardButton(text="Ховли Участка", callback_data="Xovli uchastka")],
                                    [InlineKeyboardButton(text="Ер Участкаси", callback_data="Yer uchastkasi"),
                                     InlineKeyboardButton(text="Дача ", callback_data="Dacha")]
                                ])


remontButton = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="Евроремонт", callback_data="Evroremont")],
                                        [InlineKeyboardButton(text="Таъмирланган", callback_data="Ta'mirlangan")],
                                        [InlineKeyboardButton(text="Ўртача", callback_data="O'rtacha")],
                                        [InlineKeyboardButton(text=" Таъмирсиз", callback_data="Ta'mirsiz")]
                                    ])

jihozlarButton = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="Бор", callback_data="Mavjud")],
                                        [InlineKeyboardButton(text="Йўқ", callback_data="Jihozlarsiz")]
                                    ])

valyutaButton = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="$", callback_data="USD")],
                                        [InlineKeyboardButton(text="сўм", callback_data="SUM")]
                                    ])

borYoq = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                              inline_keyboard=[
                                  [InlineKeyboardButton(text="✅ Бор", callback_data="bor"),
                                   InlineKeyboardButton(text="❌ Йўқ", callback_data="yoq")]
                              ])
