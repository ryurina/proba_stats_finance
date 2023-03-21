import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import skew, kurtosis

# import some data (NFLX: Netflix Inc stock) 
df = yf.download("NFLX")["Adj Close"].pct_change(1).dropna()

# Percentile with numpy
percentile_10 = np.quantile(df, 0.10, axis=0) * 100
print(f"Percentile 10%: {'%.2f' % percentile_10} %")

percentile_50 = np.quantile(df, 0.50, axis=0) * 100
print(f"Percentile 50%: {'%.2f' % percentile_50} %")

percentile_99 = np.quantile(df, 0.99, axis=0) * 100
print(f"Percentile 99%: {'%.2f' % percentile_99} %")
