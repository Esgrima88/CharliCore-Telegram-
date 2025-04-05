from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá, Esther! O CharliCore está vivo no Telegram!")

app = ApplicationBuilder().token("7741377039:AAHHERZOFt8-JSCF28UUXgEInpH06CldfZQ").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
        await bot.set_webhook(url=f"{RENDER_URL}/{TOKEN}")

    asyncio.run(run())
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
