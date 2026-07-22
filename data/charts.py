import pandas as pd
import yfinance as yf

COMPANY_TICKERS = {
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
}


def get_chart_data():

    frames = []

    for company, ticker in COMPANY_TICKERS.items():

        try:

            df = yf.download(
                ticker,
                period="6mo",
                interval="1d",
                auto_adjust=True,
                progress=False,
            )

            if df.empty:
                continue

            # Handle MultiIndex columns if present
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)

            df = df.reset_index()[["Date", "Close"]]
            df.rename(columns={"Close": "Price"}, inplace=True)
            df["Company"] = company

            frames.append(df)

        except Exception as e:
            print(f"{company}: {e}")

    if not frames:
        return pd.DataFrame(columns=["Date", "Price", "Company"])

    return pd.concat(frames, ignore_index=True)