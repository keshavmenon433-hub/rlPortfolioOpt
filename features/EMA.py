import yfinance as yf
import pandas as pd
import numpy as np

# EMA calculation for 20 day period
# Parameter: price returns
# Returns single column ema df
def EMA_Calc_26_Day(returns):
    total_days = len(returns)
    ema = returns.ewm(span = 26, adjust=False, min_periods = 26).mean()
    return ema
# EMA calculation for 5 day period
# Parameter: price returns
# Returns single column ema df
def EMA_Calc_5_Day(returns):
    total_days = len(returns)
    ema = returns.ewm(span = 5, adjust=False, min_periods = 26).mean()
    return ema
# EMA calculation for 12 day period
# Parameter: price returns
# Returns single column ema df
def EMA_Calc_12_Day(returns):
    total_days = len(returns)
    ema = returns.ewm(span = 12, adjust=False, min_periods = 26).mean()
    return ema
# Loads yfinance data for 11 years and 9 months of data
# Parameter: stock ticker
# returns single column returns df
def calc_returns(stock_data):
    returns = np.log(stock_data["Adj Close"] / stock_data["Adj Close"].shift(1))
    return returns
# Calculates EMA based on returns
# Parameter: stock ticker
# Returns 3 column df for 20, 5, and 12 day emas for the indicated ticker
def EMA_return(ticker):
    returns = calc_returns(ticker)
    EMA_26 = EMA_Calc_26_Day(returns).dropna()
    EMA_12 = EMA_Calc_12_Day(returns).dropna()
    EMA_5 = EMA_Calc_5_Day(returns).dropna()
    ema_total = pd.DataFrame({"EMA_26": EMA_26, "EMA_12": EMA_12, "EMA_5": EMA_5})
    ema_total = ema_total.loc[returns.expanding().count() >= 33]
    return ema_total
