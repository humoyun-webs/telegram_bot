from aiogram.dispatcher.filters.state import State,StatesGroup

class HomeKvartira(StatesGroup):
    region = State() # viloyati
    umumiyMaydon = State()
    xonalar = State()
    qavat = State()
    qavatlik = State()
    remont = State() # yevroremont, tamirlangan, o'rtacha, tamirsiz
    jihozlar = State() # jihozlar mavjud, jihozlarsiz
    gaz = State()
    svet = State()
    suv = State()
    kanalizatsiya = State()
    qoshimchaMalumot = State() # qoshimcha malumoti bo'lsa yozadi, bo'lmasa o'tkazib yuborish, majburiymas
    valyuta = State() # dollar yoki so'm,
    narxi = State()
    manzil = State() # manzil
    moljal = State() # moljal
    telNumberOne = State() # birinchi telefon yozilishi kerak
    telNumberTwo = State() # ikkinchi telefon yozilishi majburiy emas, keyingisi degan button bo'ladi
    images = State()
    check = State()

















