import time
from config import SYMBOLS
from src.signals import calculate
from src.alerts import process_alerts

while True:
    try:
        df = calculate(SYMBOLS)

        if not df.empty:
            df.to_csv("data/signals.csv", index=False)
            process_alerts(df)

        print("Scan complete")

    except Exception as e:
        print("Error:", e)

    time.sleep(900)
