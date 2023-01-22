from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import channel

channel = f"https://t.me/{channel}"

def check_user(member):
    if member["status"] != "left":
        return True
    else:
        return False


def get_check_button():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=channel)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_user")
    main.add(button1, button2)
    return main
