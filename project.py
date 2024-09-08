import yfinance as yf
import pandas as pd
import  matplotlib.pyplot as plt

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

ma_200_days = data.Close.rolling(200).mean()

plt.figure(figsize=(8,6))
plt.plot(ma_100_days, 'r')
plt.plot(ma_200_days,'b')
plt.plot(data.Close,'g')
plt.show()

data.dropna(inplace=True)

data_train = pd.DataFrame(data.Close[0: int(len(data)*0.80)])
data_test = pd.DataFrame(data.Close[int(len(data)*0.80): len(data)])
