import yfinance as yf

df = yf.download("AAPL", period="6mo", progress=False)

print(df.head())
print(df.tail())