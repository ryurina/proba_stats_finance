import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import skew, kurtosis

# import some data (NFLX: Netflix Inc stock) 
df = yf.download("NFLX")["Adj Close"].pct_change(1).dropna()

# Median with numpy
median = np.median(df, axis=0) * 100
print(f"Daily Median: {'%.2f' % median} %")
