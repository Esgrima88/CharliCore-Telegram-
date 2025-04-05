import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import logging

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
RENDER_URL = os.environ.get("RENDER_URL")

bot = Bot(token=TOKEN)

# Ativando o log para facilitar a depuração
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dp = Dispatcher(bot, None, workers=0)
    dp.add_handler(CommandHandler("start", start))
    dp.process_update(update)
    return 'ok'

@app.route('/')
def index():
    return 'CharliCore está ativo!'

def start(update, context):
    update.message.reply_text("Olá! Eu sou o CharliCore no Telegram.")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    bot.set_webhook(url=f"{RENDER_URL}/{TOKEN}")
    app.run(host="0.0.0.0", port=port)
