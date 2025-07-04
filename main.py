import os
import json
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from services.customer_service import handle_customer_message

TOKEN = os.getenv("BOT_TOKEN") or "PLACEHOLDER_TOKEN"
bot = telegram.Bot(token=TOKEN)

def start(update, context):
    update.message.reply_text("سلام! به ربات خوش اومدی 🌟")

def echo(update, context):
    user_message = update.message.text
    user_id = update.message.chat_id
    response = handle_customer_message(user_message, user_id)
    update.message.reply_text(response)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
