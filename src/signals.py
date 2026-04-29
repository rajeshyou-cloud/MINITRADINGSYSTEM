import pandas as pd
from src.fetch_data import fetch

def calculate(symbols):
    results = []

    for s in symbols:
        hist = fetch(s)

        if hist.empty:
            continue

        price = hist["Close"].iloc[-1]
        ath = hist["High"].max()
        pct = (price - ath) / ath * 100

        avg_vol = hist["Volume"].rolling(10).mean().iloc[-1]
        vol = hist["Volume"].iloc[-1]

        volume_spike = vol > 1.5 * avg_vol

        signal = "IGNORE"
        if pct >= -5 and volume_spike:
            signal = "HIGH CONVICTION"
        elif pct >= -5:
            signal = "WATCH"

        results.append([s, price, ath, pct, volume_spike, signal])

    return pd.DataFrame(results, columns=[
        "Symbol", "Price", "ATH", "%Away", "Volume Spike", "Signal"
    ])
