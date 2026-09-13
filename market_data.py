import yfinance as yf

symbol = "AAPL"  # Example stock symbol

data = yf.download(symbol, period="1mo", interval="1d")
print(data)


