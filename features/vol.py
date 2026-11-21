import yfinance as yf
import pandas as pd
import numpy as np

# Loads stock data of 11 years and 9 months for the specified ticker. Computes and returns log diffs.
# Parameters: stock ticker
# Return: log returns df
def load_returns(stock_ticker):
    stock_data = yf.download(tickers=stock_ticker, start="2015-01-01", end= "2026-10-01", auto_adjust=False, multi_level_index=False)
    returns = np.log(stock_data["Adj Close"] / stock_data["Adj Close"].shift(1))
    return returns
# Calculates rolling std
# Parameters: stock log returns
# Return: vol df
def vol_calc(returns):
    daily_vol = returns.rolling(20).std()
    daily_vol = daily_vol[returns.expanding().count() >= 26]
    return daily_vol
# Calculates vol for ticker
# Parameters: stock ticker
# Return: Vol df for ticker
def return_ticker_vol(ticker):
    ticker_vol = vol_calc(load_returns(ticker))
    return ticker_vol