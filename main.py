import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")
RENDER_URL = os.getenv("RENDER_URL")  # Ex: https://charlicore-telegram.onrender.com

bot = Bot(token=TOKEN)
app = Flask(__name__)

# Telegram application com comandos
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("CharliCore está conectado no Telegram!")

application.add_handler(CommandHandler("start", start))

@app.route("/")
def index():
    return "CharliCore está em execução!"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    application.update_queue.put_nowait(update)
    return "ok"

# Inicializa tudo
if __name__ == "__main__":
    import asyncio

    async def run():
        # Define o webhook corretamente com a URL externa
        await bot.delete_webhook()
        await bot.set_webhook(url=f"{RENDER_URL}/{TOKEN}")
        print("Webhook configurado!")

    asyncio.run(run())
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
