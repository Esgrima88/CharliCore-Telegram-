from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá, Esther! O CharliCore está vivo no Telegram!")

app = ApplicationBuilder().token("7741377039:AAHHERZOFt8-JSCF28UUXgEInpH06CldfZQ").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
