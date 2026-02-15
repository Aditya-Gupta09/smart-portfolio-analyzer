"""
Module: drawdown.py

Provides functions for calculating drawdowns.
"""

import pandas as pd


def compute_drawdown(nav_series: pd.Series) -> pd.Series:
    """
    Computes drawdown series from NAV.

    Parameters:
    nav_series (pd.Series): Portfolio net asset value series.

    Returns:
    pd.Series: Drawdown series.
    """
    running_max = nav_series.cummax()
    drawdown = (nav_series - running_max) / running_max
    return drawdown


def max_drawdown(nav_series: pd.Series) -> float:
    """
    Computes maximum drawdown.

    Parameters:
    nav_series (pd.Series): Portfolio net asset value series.

    Returns:
    float: Maximum drawdown.
    """
    drawdown_series = compute_drawdown(nav_series)
    return drawdown_series.min()
