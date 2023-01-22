from aiogram.dispatcher.filters.state import State, StatesGroup

class HomeHovli(StatesGroup):
    region = State()
    umumiyMaydon = State() # ohirida sotixda yoziladi
    xonalar = State()
    oshxona = State()
    hammom = State()
    qavatlik = State() #nechi qavatlik
    remont = State()
    jihozlar = State()
    gaz = State()
    svet = State()
    suv = State()
    kanalizatsiya = State()
    qoshimchaMalumot = State()
    valyuta = State() # $ or sum
    narxi = State()
    manzil = State()
    moljal = State()
    telNumberOne = State()
    telNumberTwo = State()
    images = State()
    check = State()