import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import skew, kurtosis

# import some data (NFLX: Netflix Inc stock) 
df = yf.download("NFLX")["Adj Close"].pct_change(1).dropna()

# L'écart-type des variations du prix d'un actif est la VOLATILITÉ

# Std with numpy
std = np.std(df, axis=0) * 100
print(f"Daily volatility: {'%.2f' % std} %")

annual_std = std * np.sqrt(252) # 252 days
print(f"Yearly volatility: {'%.2f' % annual_std} %")

monthly_std = std * np.sqrt(21) # 252 days
print(f"Monthly volatility: {'%.2f' % monthly_std} %")


