from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Telegram Bot Token
TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá, Esther! O Charli está online no Telegram.")

# Inicializa o bot
def run_bot():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

# Endpoint fake só pra manter o Render feliz
@app.route('/')
def home():
    return "Charli está vivo e funcionando."

if __name__ == '__main__':
    import threading
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
