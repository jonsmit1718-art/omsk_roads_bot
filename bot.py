import os
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Получаем токен бота из переменных окружения
TOKEN = os.getenv("8593772515:AAGQyWkY35f4SKJsHLlDxY5_CYb_2sN8NL4")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Главное меню — три кнопки
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(
    types.KeyboardButton("Сейчас"),
    types.KeyboardButton("Утро 8:00"),
    types.KeyboardButton("Вечер 17:00"),
)

async def get_fake_road_info():
    """
    Временная заглушка.
    Позже я помогу подключить реальные источники данных.
    """
    now = datetime.now().strftime("%H:%M")
    return (
        f"🚧 Дорожная информация Омска на {now}\n\n"
        "• Пробки: средние\n"
        "• Перекрытия: Ильинская — ремонт\n"
        "• ДТП: 1 мелкое на Лермонтова\n"
        "• Погода: без осадков"
    )

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет! 👋 Я бот дорожной ситуации Омска.\n"
        "Выберите время для получения сводки:",
        reply_markup=keyboard
    )

@dp.message_handler(lambda m: m.text == "Сейчас")
async def now_info(message: types.Message):
    info = await get_fake_road_info()
    await message.answer(info)

@dp.message_handler(lambda m: m.text == "Утро 8:00")
async def morning_info(message: types.Message):
    await message.answer("⏳ Получаю данные на 8:00…")
    info = await get_fake_road_info()
    await message.answer(info)

@dp.message_handler(lambda m: m.text == "Вечер 17:00")
async def evening_info(message: types.Message):
    await message.answer("⏳ Получаю данные на 17:00…")
    info = await get_fake_road_info()
    await message.answer(info)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

