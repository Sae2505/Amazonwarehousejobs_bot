import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.get(url, params={
    "chat_id": CHAT_ID,
    "text": "🔥 Bot test working from GitHub Actions"
})

print(response.status_code)
print(response.text)
