import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import skew, kurtosis

# import some data (NFLX: Netflix Inc stock) 
df = yf.download("NFLX")["Adj Close"].pct_change(1).dropna()

# Mean in numpy
mean = np.mean(df, axis=0)*100 
print(f"Daily Mean: {'%.2f' % mean} %")

# Annulization of the mean return (252 days)
annual_mean = mean * 252
print(f"Annual Mean: {'%.2f' % annual_mean} %")

# day mean return ---> monthly mean return (21 days)
monthly_mean = mean * 21
print(f"Monthly Mean: {'%.2f' % monthly_mean} %")

