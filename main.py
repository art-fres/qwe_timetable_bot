import asyncio
import os
import sys
import time
import threading
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InputMediaPhoto
from aiogram.utils.media_group import MediaGroupBuilder
from config import TOKEN, ZVONKI, PROXY
from par import filtered_links

bot = Bot(token=TOKEN)
dp = Dispatcher()

print("Bot запущен")

@dp.message(Command("start", "help"))
async def cmd_start(message: Message):
    await message.answer("Привет! В один момент нам стало лень искать ссылку на диск и спрашивать расписание в чате. А вот делать бота 2 недели лень не было, поэтому наслаждайтесь)")
    await message.answer("Разработчики- Артём Буров, Даня Киселёв")
    await message.answer('Как пользоваться?\n/help - помощь\n/timetable - расписание уроков(сегодня и завтра)\n/bells - расписание звонков\n\nВы можете добавить qwerty в группу и он будет реагировать на слово "расписание" в вашем сообщении!')


@dp.message(F.text.lower().contains("расписание"))
async def main (message: Message):
    media_group = MediaGroupBuilder()
    media_group.add_photo(media=filtered_links[0])
    media_group.add_photo(media=filtered_links[1])
    await message.reply_media_group(media=media_group.build())

#@dp.message(F.text.lower().contains("звонок"))
#async def z (message: Message):
#    photo = ZVONKI
#    await message.reply_photo(photo=photo)

    
@dp.message(Command('zvonok', "z", "zov", "zvonki", "bells"))
async def z (message: Message):
    photo = ZVONKI
    await message.reply_photo(photo=photo)

@dp.message(Command("timetable"))
async def main (message: Message):
    media_group = MediaGroupBuilder()
    media_group.add_photo(media=filtered_links[0])
    media_group.add_photo(media=filtered_links[1])
    await message.reply_media_group(media=media_group.build())

def schedule_restart():
    time.sleep(43200)
    os.execv(sys.executable, [sys.executable] + sys.argv)

async def main():
    timer_thread = threading.Thread(target=schedule_restart, daemon=True)
    timer_thread.start()
    try:
        await dp.start_polling(bot)
    except Exception as e:
        None

if __name__ == "__main__":
    
    asyncio.run(main())

