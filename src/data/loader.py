"""
Module: loader.py

Handles portfolio input loading.
"""

import pandas as pd


def load_portfolio_csv(file_path: str) -> pd.Series:
    """
    Loads portfolio CSV and returns weights as a Series.

    Expected CSV format:
    ticker,weight

    Returns:
    pd.Series indexed by ticker.
    """

    df = pd.read_csv(file_path)

    if "ticker" not in df.columns or "weight" not in df.columns:
        raise ValueError("CSV must contain 'ticker' and 'weight' columns.")

    weights = pd.Series(
        df["weight"].values,
        index=df["ticker"]
    )

    # Normalize weights
    if abs(weights.sum() - 1.0) > 1e-6:
        weights = weights / weights.sum()

    return weights
