import os
import requests

# Certifique-se de que a variável BOT_TOKEN está definida no Render
TOKEN = os.getenv("BOT_TOKEN")

# URL do seu app no Render (ajuste se mudar futuramente)
WEBHOOK_URL = f"https://charlicore-telegram-1.onrender.com/{TOKEN}"

# Endpoint da API do Telegram para configurar o webhook
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}"

# Faz a requisição
response = requests.get(TELEGRAM_API_URL)

# Exibe o resultado
print("Status:", response.status_code)
print("Resposta:", response.json())
