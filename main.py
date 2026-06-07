import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# Example Amazon Jobs (we will later improve this)
jobs = [
    {
        "title": "Amazon Warehouse Operative",
        "location": "UK",
        "link": "https://www.amazon.jobs"
    }
]

for job in jobs:
    message = f"""
🏭 Amazon Job Found!

📌 Role: {job['title']}
📍 Location: {job['location']}
🔗 Apply: {job['link']}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.get(url, params={
        "chat_id": CHAT_ID,
        "text": message
    })

print("DONE SENDING JOBS")
