import yfinance as yf
import pandas as pd
import numpy as np

def load_returns(stock_ticker):
    vix = yf.download(vix, start="2015-01-01", end= "2026-10-01", auto_adjust=False, multi_level_index=False)
    return vix['Close']