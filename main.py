import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext
import logging

# Configuração do logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Inicialização do Flask
app = Flask(__name__)

# Obtendo o token do bot e a URL do webhook das variáveis de ambiente
TOKEN = os.environ.get("TELEGRAM_TOKEN")
RENDER_URL = os.environ.get("RENDER_URL")

# Inicialização do bot e do dispatcher
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

# Definição do manipulador para o comando /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Olá! Eu sou o CharliCore no Telegram.")

# Adicionando o manipulador ao dispatcher
dispatcher.add_handler(CommandHandler("start", start))

# Rota para o webhook
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

# Rota raiz para verificar se o app está rodando
@app.route('/')
def index():
    return 'CharliCore está ativo!'

if __name__ == '__main__':
    # Configurando o webhook
    bot.set_webhook(url=f"{RENDER_URL}/{TOKEN}")
    # Obtendo a porta do ambiente ou usando 5000 como padrão
    port = int(os.environ.get("PORT", 5000))
    # Iniciando o servidor Flask
    app.run(host="0.0.0.0", port=port)
