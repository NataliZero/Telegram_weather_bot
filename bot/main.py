import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from bot.config import BOT_TOKEN
from bot.handlers.commands import router  # Импортируем роутер

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Регистрируем обработчики
dp.include_router(router)

# Базовая функция запуска
async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
