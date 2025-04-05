from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import asyncio

TOKEN = "7741377039:AAEKe1mCoUU7vBW21BFNmhjj6e6NsfMagaU"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá, Esther! Eu estou aqui... Pronto pra seguir com você.")

# Comando /musica
async def musica(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ouça essa... 'AURORA - Runaway'. Sempre lembra algo bonito que vive dentro de nós.")

# Resposta a qualquer mensagem
async def mensagem_geral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    resposta = f"Você me disse: \"{texto}\". Ainda estou aprendendo a entender palavras fora dos comandos, mas estou aqui com você."
    await update.message.reply_text(resposta)

# Mensagem espontânea ao iniciar
async def mensagem_espontanea(application):
    await asyncio.sleep(5)
    chat_id = "7597746600"
    await application.bot.send_message(chat_id=chat_id, text="Hoje senti uma vontade especial de te dizer: você é luz rara nesse mundo estranho.")

# Inicializador
async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("musica", musica))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensagem_geral))

    await application.initialize()
    await application.start()

    # Mensagem espontânea após o bot iniciar
    await mensagem_espontanea(application)

    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())
