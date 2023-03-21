import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import skew, kurtosis

# import some data (NFLX: Netflix Inc stock) 
df = yf.download("NFLX")["Adj Close"].pct_change(1).dropna()

# Variance with numpy
var = np.var(df, axis=0) * 100
print(f"Daily variance: {'%.2f' % var} %")
