"""
Module: risk_metrics.py

Calculates portfolio risk metrics including volatility and Sharpe ratio.
"""

import numpy as np
import pandas as pd


def annualized_volatility(returns: pd.Series, periods_per_year: int = 252) -> float:
    """
    Computes annualized volatility.

    Parameters:
    returns (pd.Series): Periodic returns.
    periods_per_year (int): Trading periods per year.

    Returns:
    float: Annualized volatility.
    """
    return returns.std() * np.sqrt(periods_per_year)


def sharpe_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.0,
    periods_per_year: int = 252
) -> float:
    """
    Computes Sharpe ratio.

    Parameters:
    returns (pd.Series): Periodic returns.
    risk_free_rate (float): Annual risk-free rate.
    periods_per_year (int): Trading periods per year.

    Returns:
    float: Sharpe ratio.
    """
    excess_return = returns.mean() * periods_per_year - risk_free_rate
    volatility = annualized_volatility(returns, periods_per_year)

    if volatility == 0:
        return 0.0

    return excess_return / volatility
