import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

r = requests.get(url, params={
    "chat_id": CHAT_ID,
    "text": "TEST FROM GITHUB ACTION 🚀"
})

print("STATUS CODE:", r.status_code)
print("RESPONSE:", r.text)
