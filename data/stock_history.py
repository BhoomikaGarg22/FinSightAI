import pandas as pd
import yfinance as yf


def get_stock_history(ticker):
    try:
        df = yf.download(
            ticker,
            period="6mo",
            interval="1d",
            auto_adjust=True,
            progress=False,
        )

        if df.empty:
            return None

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df.reset_index()[["Date", "Close"]]
        df.columns = ["Date", "Price"]

        return df

    except Exception as e:
        print(e)
        return None