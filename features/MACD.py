import yfinance as yf
import pandas as pd
import numpy as np
from .EMA import EMA_Calc_12_Day, EMA_Calc_26_Day

# Loads yfinance data for 11 years and 9 months of data
# Parameter: stock ticker
# Returns single column adjusted close price df
def load_prices(stock_ticker):
    stock_data = yf.download(tickers=stock_ticker, start="2015-01-01", end= "2026-10-01", auto_adjust=False, multi_level_index=False)
    prices = stock_data["Adj Close"]
    return prices
# Calculates MACD for specific ticker comparing 12 and 26 period EMAs of price
# Parameters: stock ticker
# Return: MACD calculation df of MACD line and histogram
def MACD_Calc(tick):
    prices = load_prices(tick)
    EMA_12 = EMA_Calc_12_Day(prices)
    EMA_26 = EMA_Calc_26_Day(prices)
    MACD_line = (EMA_12-EMA_26)/EMA_26
    signal_line = MACD_line.ewm(span=9, adjust = False, min_periods=9).mean()
    histogram = MACD_line - signal_line
    MACD_data = pd.DataFrame({"MACD": MACD_line, "histogram": histogram})
    MACD_data = MACD_data[prices.expanding().count() >= 34]
    return MACD_data
