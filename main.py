from email import message
from mailbox import Message
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.update import Update
import settings
import requests
from telegram.ext.filters import Filters

updater = Updater(token=settings.TELEGRAM_TOKEN)

def start(update: Update, context: CallbackContext):
    update.message\
        .reply_text('Assalomu Alaykum! Raxmatjonning Wiki Search botiga hush kelibsiz. Biron nima izlash uchun /search va so\'rovingizni yozing. Misol uchun: /search Saturn\n\nKanalimiz: @ufobots')


def search(update: Update, context: CallbackContext):
    args = context.args
    if len(args) == 0:
        update.message.reply_text("Hech bo'lmasa nimadir kiriting. Misol uchun /search Saturn")
    else:
        search_text = ' '.join(args)
        res = requests.get('https://uz.wikipedia.org/w/api.php', {
            'action':'opensearch',
            'search': search_text,
            'limit':1,
            'format':'json',
        })
        result = res.json()
        link = result[3]

        if len(link):
            update.message.reply_text("Sining so'rovingiz bo'yicha havola: "+link[0])
        else:
            update.message.reply_text("Sining so'rovingiz bo'yicha hech nima topilmadi")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
dispatcher.add_handler(MessageHandler(Filters.all, start))

updater.start_polling()
updater.idle()