import yfinance as yf
import pandas as pd
import numpy as np

# Loads stock data of 11 years and 9 months for the specified ticker. Computes and returns log diffs.
# Parameters: stock ticker
# Return: log returns df
def load_returns(stock_data):
    returns = np.log(stock_data['Adj Close']/stock_data['Adj Close'].shift(60))
    return returns

