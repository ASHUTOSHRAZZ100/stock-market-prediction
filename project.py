import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

start = '2014-01-01'
end = '2024-08-30'
stock = 'GOOG'

data = yf.download(stock, start, end)

print(data)

data.reset_index(inplace=True)

print(data)

ma_100_days = data.Close.rolling(100).mean()

plt.figure(figsize=(8,6))
plt.plot(ma_100_days, 'r')
plt.plot(data.Close, 'g')
plt.show()