from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from bot.utils.weather import get_weather  # Импортируем функцию для погоды

router = Router()

@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer("Привет! Я бот, который отправляет прогноз погоды. Напиши /help, чтобы узнать мои команды.")

@router.message(Command("help"))
async def command_help(message: Message):
    await message.answer("Вот список моих команд:\n/start - Начать работу\n/help - Список команд\n/weather - Прогноз погоды для Санкт-Петербурга")

@router.message(Command("weather"))
async def command_weather(message: Message):
    weather_info = get_weather()  # Получаем информацию о погоде
    await message.answer(weather_info)  # Отправляем информацию пользователю
