import asyncio
from aiogram import Bot, Dispatcher
from bot.config import BOT_TOKEN  # Импорт токена из файла config.py
from bot.handlers.commands import router  # Импорт роутера из handlers.commands

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
