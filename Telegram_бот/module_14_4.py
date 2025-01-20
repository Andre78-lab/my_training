from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from crud_functions import get_all_products

import asyncio

api = "№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рассчитать"),
            KeyboardButton(text="Информация")
        ],
        [
            KeyboardButton(text="Купить")
        ]
    ], resize_keyboard=True
)

kb_in = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
        ]
    ]
)

kb_in_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 4', callback_data='product_buying'),

        ]
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer(text='Выберите опцию:', reply_markup=kb_in)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10*вес(кг) + 6,25*рост(см) – 5*возраст(г) + 5\n'
                              'для женщин: 10*вес(кг) + 6,25*рост(см) – 5*возраст(г) – 161')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f'Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(
        f'Если вы мужчина: {round(10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) + 5)} норма калорий для потребления')
    await message.answer(
        f'Если вы женщина: {round(10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) - 161)} норма калорий для потребления')
    await state.finish()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    name_product = get_all_products()

    for i in range(len(name_product)):
        if i < 4:
            with open(f'imgs/Product{i+1}.jpg', 'rb') as img:
                await message.answer_photo(img,
                                           f'Название: {name_product[i][1]} | Описание: {name_product[i][2]} | Цена: {name_product[i][3]}')
        else:
            await message.answer(f'Название: {name_product[i][1]} | Описание: {name_product[i][2]} | Цена: {name_product[i][3]}')

    await message.answer(text='Выберите продукт для покупки:', reply_markup=kb_in_buy)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(commands=['start'])
async def start_commands(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":

    executor.start_polling(dp, skip_updates=True)

