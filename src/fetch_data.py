import yfinance as yf

def fetch(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="6mo")
