import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import skew, kurtosis

portfolio = ["GOOG", "TSLA", "META", "AMZN"]
df = yf.download(portfolio)["Adj Close"].pct_change(1).dropna()

print(df.corr())

