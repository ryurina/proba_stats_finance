import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import skew, kurtosis

#portfolio = ["BTC-USD", "ETH-USD"]
portfolio = ["GOOG", "AAPL", "META", "AMZN"]

df = yf.download(portfolio)["Adj Close"].pct_change(1).dropna()

# Variance Covariance matrix
mat = np.cov(df, rowvar=False)

print(pd.DataFrame(mat, columns=df.columns, index=df.columns))

# -1 < corr < 0: Correlation negative
# corr = 0: Aucune correlation
# 0 < corr < 1: Correlation positive
