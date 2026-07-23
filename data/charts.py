import pandas as pd
import yfinance as yf

COMPANY_TICKERS = {
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
}

def get_chart_data(company=None):

    frames = []

    companies = (
        {company: COMPANY_TICKERS[company]}
        if company and company in COMPANY_TICKERS
        else COMPANY_TICKERS
    )

    for company_name, ticker in companies.items():

        try:

            df = yf.download(
                ticker,
                period="30d",
                interval="1d",
                auto_adjust=True,
                progress=False,
            )

            if df.empty:
                continue

            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)

            df = df.reset_index()

            df = df[["Date", "Close"]]

            df.rename(columns={"Close": "Price"}, inplace=True)

            df["Company"] = company_name

            frames.append(df)

        except Exception as e:
            print(e)

    if not frames:
        return pd.DataFrame(columns=["Date", "Price", "Company"])

    return pd.concat(frames, ignore_index=True)