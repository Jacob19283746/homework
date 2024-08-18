from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from config import api

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button2 = KeyboardButton(text='Информация')
button = KeyboardButton(text='Расчитать')
kb.row(button, button2)

kb2 = InlineKeyboardMarkup()
in_but = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
in_but2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.add(in_but, in_but2)


@dp.message_handler(commands=['Start'])
async def start(message):
    await message.answer('Привет!', reply_markup=kb)


@dp.message_handler(text='Расчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Я бот "Здоровье". Я могу расчитать калории на основе твоего веса, роста и возраста, '
                         'если хочешь попробывать нажми кнопку |Расчитать|.')


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
