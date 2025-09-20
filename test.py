import asyncio
import logging
import os
import sys
import time
import threading
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, ZVONKI, PROXY
from par import filtered_links

bot = Bot(token=TOKEN)
dp = Dispatcher()

print("Bot запущен")

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Профиль", callback_data="profile")],
        [InlineKeyboardButton(text="Настройки", callback_data="settings")],
        [InlineKeyboardButton(text="Помощь", callback_data="help")]
    ])

def get_settings_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Изменить класс", callback_data="settings")]
    ])

def get_class_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Изменить класс", callback_data="class")]
    ])

def get_canteen_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Да", callback_data="canteen_yes")],
        [InlineKeyboardButton(text="Нет", callback_data="canteen_no")]
    ])



@dp.message(Command("start", "menu"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Главное меню:",
        reply_markup=get_main_keyboard()
    )

class_number = "Не выбран"
@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    data = callback.data
    
    if data == "profile":
        await callback.message.edit_text("Ваш профиль:\nКласс: "+ class_number)
        await callback.answer()
    
    elif data == "settings":
    
        await callback.message.answer(
        "Выберите ваш класс:",
        reply_markup=get_class_keyboard()
    )
    
    await callback.message.answer(
        "Напоминать про столовую?\n"
        "(На перемене, во время которой у вашего класса должна быть столовая, "
        "бот напишет вам напоминание)",
        reply_markup=get_canteen_keyboard()
    )
        

@dp.message(Command('photo'))
async def main (message: Message):
    photo = filtered_links[0]
    await message.reply_photo(photo=photo)

@dp.message(Command('zvonok', "z", "zov"))
async def main (message: Message):
    photo = ZVONKI
    await message.reply_photo(photo=photo)
        


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
