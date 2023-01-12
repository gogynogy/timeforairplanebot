from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMedia, CallbackQuery
import buttons as but
from message import give_time_delta, get_image
from users import admins, geo
from loader import bot
from loader import dp





@dp.message_handler(commands="start")  # /start command processing
async def begin(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1).add(but.refresh)
    await bot.send_photo(chat_id=message.chat.id,
                         photo=get_image(),
                         caption=give_time_delta(),
                         reply_markup=keyboard)
    await bot.send_message(chat_id=geo,
                           text=f"{message.chat.username}")


@dp.callback_query_handler(lambda c: c.data == "Refresh")
async def refresh(query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=1).add(but.refresh)
    file = InputMedia(media=get_image(), caption=give_time_delta())
    await query.message.edit_media(file, reply_markup=keyboard)
    await bot.send_message(chat_id=geo,
                           text=f"{query.message.chat.username}")