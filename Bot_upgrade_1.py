import os.path

from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions_upgrade_1 import initiate_db, is_included, add_user, get_all_products
from config import api

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
initiate_db()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button2 = KeyboardButton(text='Информация')
button = KeyboardButton(text='Расчитать')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
kb.row(button, button3, button2, button4)

kb2 = InlineKeyboardMarkup()
in_but = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
in_but2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.add(in_but, in_but2)

kb3 = InlineKeyboardMarkup()
products = get_all_products()
for product in products:
    kb3.row(InlineKeyboardButton(text=product[1], callback_data='product_buying'))


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@dp.message_handler(commands=['Start'])
async def start(message):
    await message.answer('Привет!', reply_markup=kb)


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.message, state: FSMContext):
    username = message.text
    if not is_included(username):
        await state.update_data(username=username)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = int(message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], age)
    await message.answer("Регистрация завершена!")
    await state.finish()


@dp.message_handler(text='Расчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for i, product in enumerate(products):
        product_info = f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}'
        await message.answer(product_info)
        try:
            with open(f'image/{i + 1}.jpg', 'rb') as img:
                await message.answer_photo(img)
        except FileNotFoundError:
            await message.answer('Изображение не найдено.')

    await message.answer('Выберите продукт для покупки:', reply_markup=kb3)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(f'Вы приобрели продукт!')
    await call.answer()


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Я бот "Здоровье". Я могу расчитать калории на основе твоего веса, роста и возраста,'
                         'а также ты можешь приобрести витамины'
                         'если хочешь расчитать калории нажми кнопку |Расчитать|, '
                         'если хочешь приобрести витамины нажми |Купить|.')


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def start_calories(call):
    await UserState.age.set()
    await call.message.answer("Введите свой возраст:")
    await call.answer()


@dp.message_handler(state=UserState.age)
async def process_age(message: types.Message):
    age = int(message.text)
    await UserState.growth.set()
    await message.answer("Введите свой рост в сантиметрах:")


@dp.message_handler(state=UserState.growth)
async def process_growth(message: types.Message):
    growth = int(message.text)
    await UserState.weight.set()
    await message.answer("Введите свой вес в килограммах:")


@dp.message_handler(state=UserState.weight)
async def process_weight(message: types.Message):
    weight = int(message.text)

    age = 25
    growth = 175
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша суточная норма калорий: {calories:.2f} ккал")
    await dp.current_state(user=message.from_user.id).finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)