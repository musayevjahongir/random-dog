from telegram import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='DOG🐶')
        ]
        
    ],
    resize_keyboard = True
)