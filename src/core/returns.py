"""
Module: returns.py

Handles portfolio return calculations and annualization logic.
"""

import pandas as pd


def compute_periodic_returns(price_series: pd.Series) -> pd.Series:
    """
    Computes periodic returns from price series.

    Parameters:
    price_series (pd.Series): Adjusted closing prices.

    Returns:
    pd.Series: Periodic returns.
    """
    return price_series.pct_change().dropna()


def annualize_returns(returns: pd.Series, periods_per_year: int = 252) -> float:
    """
    Annualizes periodic returns.

    Parameters:
    returns (pd.Series): Periodic returns.
    periods_per_year (int): Number of periods in a year.

    Returns:
    float: Annualized return.
    """
    compounded_growth = (1 + returns).prod()
    n_periods = len(returns)

    if n_periods == 0:
        return 0.0

    return compounded_growth ** (periods_per_year / n_periods) - 1
