import yfinance as yf
import pandas as pd
import numpy as np

# Loads stock data of 11 years and 9 months for the specified ticker. Computes and returns log diffs.
# Parameters: stock ticker
# Return: log returns df
def load_returns(stock_ticker):
    stock_data = yf.download(tickers=stock_ticker, start="2015-01-01", end= "2026-10-01", auto_adjust=False, multi_level_index=False)
    returns = np.log(stock_data['Adj Close']/stock_data['Adj Close'].shift(60))
    returns_data = [{"returns":returns, "dates":stock_data}]

