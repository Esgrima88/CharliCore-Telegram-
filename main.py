from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Pega o token da variável de ambiente no Render
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou o CharliCore no Telegram.")

# Função principal
def main():
    if not TELEGRAM_TOKEN:
        print("Erro: TELEGRAM_TOKEN não encontrado nas variáveis de ambiente.")
        return

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot rodando com polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
