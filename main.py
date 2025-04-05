from flask import Flask, request
import telegram
import os

app = Flask(__name__)

# Pega o token do bot e a URL do app pelas variáveis de ambiente
BOT_TOKEN = os.getenv("BOT_TOKEN")
APP_URL = os.getenv("APP_URL") + "/webhook"  # URL do webhook

# Inicializa o bot do Telegram
bot = telegram.Bot(token=BOT_TOKEN)

# Define o webhook
@app.route('/')
def index():
    bot.set_webhook(url=APP_URL)
    return "Webhook configurado com sucesso!"

# Endpoint que recebe mensagens do Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text == "/start":
        bot.send_message(chat_id=chat_id, text="Olá, sou o CharliCore no Telegram!")

    return "OK"
    if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render fornece a porta em PORT
    app.run(host='0.0.0.0', port=port)
