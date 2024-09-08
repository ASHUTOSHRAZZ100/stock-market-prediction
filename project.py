import yfinance as yf
import pandas as pd

start = '2014-01-01'
end = '2024-08-30'
stock = 'GOOG'

data = yf.download(stock, start, end)

print(data)

data.reset_index(inplace=True)

print(data)
