"""
Module: attribution.py

Handles portfolio attribution and exposure calculations.
"""

import pandas as pd


def sector_exposure(weights: pd.Series, sector_map: dict) -> dict:
    """
    Aggregates portfolio weights by sector.

    Parameters:
    weights (pd.Series): Portfolio weights indexed by ticker.
    sector_map (dict): Mapping of ticker to sector.

    Returns:
    dict: Sector exposure distribution.
    """
    exposure = {}

    for ticker, weight in weights.items():
        sector = sector_map.get(ticker, "Unknown")
        exposure[sector] = exposure.get(sector, 0) + weight

    return exposure


def simple_benchmark_comparison(
    portfolio_returns: pd.Series,
    benchmark_returns: pd.Series
) -> float:
    """
    Computes excess return versus benchmark.

    Returns:
    float: Excess annualized return.
    """
    portfolio_ann = (1 + portfolio_returns).prod() - 1
    benchmark_ann = (1 + benchmark_returns).prod() - 1

    return portfolio_ann - benchmark_ann
