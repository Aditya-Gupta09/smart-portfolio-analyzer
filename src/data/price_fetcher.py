"""
Module: price_fetcher.py

Responsible for retrieving market price data.
"""

import yfinance as yf
import pandas as pd


def fetch_adjusted_close(
    tickers: list,
    start: str = "2023-01-01",
    end: str = None
) -> pd.DataFrame:
    """
    Fetches adjusted closing prices for given tickers.

    Parameters:
    tickers (list): List of ticker symbols.
    start (str): Start date (YYYY-MM-DD).
    end (str): End date (YYYY-MM-DD).

    Returns:
    pd.DataFrame: Adjusted close price data.
    """

    data = yf.download(
        tickers,
        start=start,
        end=end,
        progress=False
    )["Adj Close"]

    if isinstance(data, pd.Series):
        data = data.to_frame()

    return data.dropna(how="all")
