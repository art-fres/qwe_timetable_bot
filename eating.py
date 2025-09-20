import asyncio
import logging
from datetime import datetime, time, timedelta
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
users = set()

@dp.message(Command("start"))
async def start_handler(message: Message):
    users.add(message.from_user.id)
    await message.answer("Бот запущен! Вы будете получать уведомления о столовой.")

@dp.message(Command("users"))
async def users_handler(message: Message):
    await message.answer(f"Всего пользователей: {len(users)}")

async def send_daily_notification():
    for user_id in list(users):
        await bot.send_message(user_id, "Сейчас столовка! 🍽")
        
async def scheduler():
    
    while True:
        now = datetime.now()
        
        
        target_time = datetime(now.year, now.month, now.day, 17, 28)
        if now > target_time:
            target_time += timedelta(days=1)
        
       
        while target_time.weekday() >= 5:  
            target_time += timedelta(days=1)
        
        
        wait_seconds = (target_time - now).total_seconds()
        print(f"Следующее уведомление в {target_time}, ждем {wait_seconds} секунд")
        
        if wait_seconds > 0:
            await asyncio.sleep(wait_seconds)
        await send_daily_notification()
        await asyncio.sleep(60)

async def main():
    asyncio.create_task(scheduler())
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())