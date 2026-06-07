import requests

BOT_TOKEN = "PASTE_NEW_TOKEN_HERE"
CHAT_ID = "8590592063"

requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": "Direct test message 🚀"
    }
)

print("done")
