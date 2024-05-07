import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from config import config
from handlers import reg

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",)
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(token=config.bot_token.get_secret_value())

    dp.include_router(reg.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


    

if __name__ == "__main__":
    asyncio.run(main())