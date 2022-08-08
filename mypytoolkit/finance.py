"""
Operations related to money.
"""
# External imports 
import numpy as np

# Local imports
from typing import Callable
import math

# Project modules
from . import dates


def sharpe_ratio(returns: list, risk_free: float) -> float:
    """
    Calculates the sharpe ratio of a list of returns.
    Returns must be a list, and risk free rate is required.
    """
    # STD and mean
    returns_std = np.std(returns)
    returns_mean = np.mean(returns)

    return (returns_mean - risk_free) / returns_std


# ---- Market clock ----

last_market_open_verification = 0.00

def market_open(market_clock_func: Callable[[], bool]) -> bool:
    """
    Smart algorithm to determine if the market is open.
    Minimize API calls due to rate limits. Based on the assumption that the 
    market will never close during any 15-minute window. For ex., the market
    will never close at 3:13pm, but there's a small chance it could close at 3:15pm.

    Call this function as many times as you want, or in a while loop, and it will only
    call the function you pass in a handful of times, at most once every fifteen minutes.

    Pass in a function that when called returns a simple boolean of whether the market is open.
    This function should make an API call to your preferred broker or data provider.
    """
    global last_market_open_verification  # for speeding up market clock
    
    if 1 <= dates.weekday_int() <= 5 and 9.5 < dates.time_decimal() < 16:
        if(
            # same hour
            math.floor(dates.time_decimal()) == math.floor(last_market_open_verification)
            # last_time and time_decimal_decimal are in the same 30 minute window \
                # (0,30) or (30, 60)
            and math.ceil(round(dates.time_decimal() % 1, 5) * 2) == \
                math.ceil((round(last_market_open_verification % 1, 5)) * 2)
        ):
            return True
        elif market_clock_func():
            last_market_open_verification = dates.time_decimal()
            return True
            
    # If none
    return False
