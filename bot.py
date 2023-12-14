from settings import TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import (
    start,
    echo_photo
)


def main():
    # create updater obj.
    updater = Updater(TOKEN)
    
    # create dispatcher obj.
    dispatcher = updater.dispatcher
    
    # add command handlers
    dispatcher.add_handler(
        handler=CommandHandler(
            command=['start', 'boshlash'], 
            callback=start
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("DOG🐶"),
            callback=echo_photo
        )
    )

    # start polling
    updater.start_polling()
    updater.idle()

main()