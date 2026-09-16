
import pandas as pd
import yfinance as yf
import streamlit as st


COMPANY_TICKERS = {
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
}


@st.cache_data(ttl=300)
def get_chart_data(company=None):

    if company and company in COMPANY_TICKERS:
        selected_companies = {company: COMPANY_TICKERS[company]}
    else:
        selected_companies = COMPANY_TICKERS

    frames = []

    for company_name, ticker in selected_companies.items():

        try:
            df = yf.download(
                ticker,
                period="1mo",
                interval="1d",
                auto_adjust=True,
                progress=False,
                threads=False,
            )

            if df.empty:
                continue

            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)

            df = df.reset_index()

            df = df[["Date", "Close"]].copy()

            df.rename(
                columns={"Close": "Price"},
                inplace=True,
            )

            df["Company"] = company_name

            frames.append(df)

        except Exception as e:
            print(f"Error fetching {company_name}: {e}")

    if not frames:
        return pd.DataFrame(
            columns=["Date", "Price", "Company"]
        )

    return pd.concat(frames, ignore_index=True)


def get_latest_stock_price(company):

    ticker = COMPANY_TICKERS.get(company)

    if not ticker:
        return None, None

    try:
        stock = yf.Ticker(ticker)

        # Try to get recent intraday prices
        df = stock.history(
            period="1d",
            interval="1m"
        )

        # Fall back to the latest daily closing prices
        if df.empty:
            df = stock.history(
                period="5d",
                interval="1d"
            )

        if df.empty:
            return None, None

        prices = df["Close"].dropna()

        if prices.empty:
            return None, None

        latest_price = float(prices.iloc[-1])

        # Calculate change from the previous available price
        if len(prices) >= 2:
            previous_price = float(prices.iloc[-2])

            if previous_price != 0:
                change = (
                    (latest_price - previous_price)
                    / previous_price
                ) * 100
            else:
                change = None
        else:
            change = None

        return latest_price, change

    except Exception as e:
        print(f"Error fetching price for {company}: {e}")
        return None, None

    
@st.cache_data(ttl=900)
def get_live_company_stats(company):

    ticker = COMPANY_TICKERS.get(company)

    if not ticker:
        return {}

    try:
        info = yf.Ticker(ticker).info

        market_cap = info.get("marketCap")
        pe_ratio = info.get("trailingPE")
        high_52 = info.get("fiftyTwoWeekHigh")

        return {
            "market_cap": (
                f"${market_cap / 1_000_000_000:,.2f}B"
                if market_cap else "Unavailable"
            ),
            "pe_ratio": (
                f"{pe_ratio:.2f}"
                if pe_ratio is not None else "Unavailable"
            ),
            "high_52": (
                f"${high_52:,.2f}"
                if high_52 is not None else "Unavailable"
            ),
        }

    except Exception as e:
        print(f"Error fetching stats for {company}: {e}")
        return {}

    
@st.cache_data(ttl=300)
def get_technical_indicators(company):

    ticker = COMPANY_TICKERS.get(company)

    if not ticker:
        return {}

    try:
        df = yf.Ticker(ticker).history(
            period="3mo",
            interval="1d",
            auto_adjust=True
        )

        if df.empty or "Close" not in df:
            return {}

        close = df["Close"].dropna()

        if len(close) < 26:
            return {}

        # RSI (14-day)
        delta = close.diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(14).mean()
        avg_loss = loss.rolling(14).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        # 20-day simple moving average
        moving_average = close.rolling(20).mean()

        # MACD (12-day EMA - 26-day EMA)
        ema_12 = close.ewm(span=12, adjust=False).mean()
        ema_26 = close.ewm(span=26, adjust=False).mean()
        macd = ema_12 - ema_26

        return {
            "rsi": (
                f"{rsi.iloc[-1]:.2f}"
                if pd.notna(rsi.iloc[-1])
                else "Unavailable"
            ),
            "moving_average": (
                f"${moving_average.iloc[-1]:,.2f}"
                if pd.notna(moving_average.iloc[-1])
                else "Unavailable"
            ),
            "macd": (
                f"{macd.iloc[-1]:.2f}"
                if pd.notna(macd.iloc[-1])
                else "Unavailable"
            ),
        }

    except Exception as e:
        print(f"Error calculating indicators for {company}: {e}")
        return {}