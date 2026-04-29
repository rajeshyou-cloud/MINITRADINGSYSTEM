import requests
from config import *

def send_telegram(msg):
    if not TELEGRAM_TOKEN:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg})

def process_alerts(df):
    for _, row in df.iterrows():
        if row["Signal"] == "HIGH CONVICTION":
            send_telegram(f"{row['Symbol']} breakout 🚀")
