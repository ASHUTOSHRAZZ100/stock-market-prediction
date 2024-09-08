import yfinance as yf

start = '2014-01-01'
end = '2024-08-30'
stock = 'GOOG'

data = yf.download(stock, start, end)