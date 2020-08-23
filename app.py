from spacex_py import launches
import logging
import requests

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN # Your config with bot api token


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Buttons
btn_next = KeyboardButton("/next_launch")
btn_last = KeyboardButton("/last_launch")

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_last)
greet_kb.add(btn_next)

# /Start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello!", reply_markup=greet_kb)

# /Next Launch
@dp.message_handler(commands=['next_launch'])
async def NextLaunchData(massage: types.message):
    mission, header= launches.get_next_launch()
    name = mission['mission_name']
    year = mission['launch_year']
    date = mission['launch_date_utc']
    rocket = mission['rocket']['rocket_name']
    await massage.answer("Mission name: " + name + "\nYear of launch: " + year + "\nLaunch date: " + date + "\nRocket: " + rocket, reply_markup=greet_kb)

# /Last Launch
@dp.message_handler(commands=['last_launch'])
async def LastLaunchData(massage: types.message):
    mission, header= launches.get_latest_launch()
    name = mission['mission_name']
    year = mission['launch_year']
    date = mission['launch_date_utc']
    rocket = mission['rocket']['rocket_name']
    await massage.answer("Mission name: " + name + "\nYear of launch: " + year + "\nLaunch date: " + date + "\nRocket: " + rocket, reply_markup=greet_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

