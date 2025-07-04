import os
import json
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from services.customer_service import handle_customer_message

# توکن مستقیم (در حالت لوکال یا ساده‌سازی اولیه استفاده میشه)
TOKEN = "7847661218:AAEIHUcwg2gb7jF8zdK75w2Xk_exIewWAPU"

bot = telegram.Bot(token=TOKEN)

def start(update, context):
    update.message.reply_text("سلام! به ربات CRM خوش اومدی 🌟\nچطور می‌تونم کمکت کنم؟")

def echo(update, context):
    user_message = update.message.text
    response = handle_customer_message(user_message)
    update.message.reply_text(response)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
