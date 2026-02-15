"""
Module: sector_mapper.py

Maps tickers to sectors.
"""

import pandas as pd


def load_sector_map(file_path: str) -> dict:
    """
    Loads sector mapping CSV.

    Expected format:
    ticker,sector

    Returns:
    dict mapping ticker -> sector
    """

    df = pd.read_csv(file_path)

    if "ticker" not in df.columns or "sector" not in df.columns:
        raise ValueError("Sector map CSV must contain 'ticker' and 'sector' columns.")

    return dict(zip(df["ticker"], df["sector"]))
