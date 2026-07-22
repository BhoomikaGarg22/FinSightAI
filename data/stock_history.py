import yfinance as yf
import pandas as pd
import streamlit as st

def get_stock_history(ticker):
    try:
        st.write("Ticker:", ticker)

        df = yf.download(
            ticker,
            period="6mo",
            interval="1d",
            auto_adjust=True,
            progress=False,
        )

        st.write("Columns:", df.columns)
        st.write(df.head())

        if df.empty:
            st.error("DataFrame is empty")
            return None

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df.reset_index()

        st.write(df.head())

        return pd.DataFrame({
            "Date": df["Date"],
            "Price": df["Close"]
        })

    except Exception as e:
        st.exception(e)
        return None