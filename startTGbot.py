import logging
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
logging.basicConfig(format ='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(update: Updater, context: CallbackContext):
    mytext = """Hello {}
    I have onli /start command(((""".format(update.message.chat.first_name)
    update.message.reply_text(mytext)
    print("Hello")

def chat(update: Updater, context: CallbackContext):
    text = "hello"

    update.message.reply_text(text) 

def main():
    updtr = Updater('') #token

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    updtr.start_polling()
    updtr.idle()

if __name__ == '__main__':
    logging.info('bot started!')
    main()