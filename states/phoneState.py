from aiogram.dispatcher.filters.state import State, StatesGroup

class Telephone(StatesGroup):
    model = State()  # masalan: Samsung a13
    memory = State()  # xotirasi
    color = State()  # masalan: qizil, qora, oq
    status = State()  # masalan: Yangi, Yaxshi, Ideal, Eski
    documents = State()  # hujatlari bor yoki yoqligi
    price = State()  # masalan: 350$, 2mln
    phone = State()  # masalan: +9989002911088
    senderNumber = State()  # jonatilayotgan nomer telegramda
    region = State()  # masalan: toshkent, andijon
    info = State()  # masalan: obmen bor yoki yo'q, telefon haqida to'liq malumot
    images = State()  # masalan: telefoningizni 5 tagacha suratini joylashiningiz mumkin
    check = State()
