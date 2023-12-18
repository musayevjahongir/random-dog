from telegram.ext import CallbackContext
from telegram import Update
from keyboards import start_keyboard
from settings import URL
import requests

def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    bot = context.bot

    bot.sendMessage(user.id, 'Asslomu alaykum.', reply_markup=start_keyboard)

def echo_photo(update: Update, context: CallbackContext):
    user = update.message.from_user

    photo = requests.get(URL).json()



    bot = context.bot

    bot.sendPhoto(user.id, photo["url"])
