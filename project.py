import yfinance as yf
import pandas as pd
import  matplotlib.pyplot as plt
import numpy as np

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

data_train.shape[0]
data_test.shape[0]

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

data_train_scale = scaler.fit_transform(data_train)

x = []
y = []

for i in range(100, data_train_scale.shape[0]):
    x.append(data_train_scale[i-100:i])
    y.append(data_train_scale[i,0])

x, y = np.array(x), np.array(y)

from keras.layers import Dense, Dropout, LSTM
from keras.models import Sequential

model = Sequential()
model.add(LSTM(units = 50, activation = 'relu', return_sequences = True,
               input_shape = ((x.shape[1],1))))
model.add(Dropout(0.2))

model.add(LSTM(units = 60, activation='relu', return_sequences = True))
model.add(Dropout(0.3))

model.add(LSTM(units = 80, activation = 'relu', return_sequences = True))
model.add(Dropout(0.4))

model.add(LSTM(units = 120, activation = 'relu'))
model.add(Dropout(0.5))

model.add(Dense(units =1))

model.compile(optimizer = 'adam', loss = 'mean_squared_error')

model.fit(x,y, epochs = 50, batch_size =32, verbose =1)

model.summary()

pas_100_days = data_train.tail(100)

data_test = pd.concat([pas_100_days, data_test], ignore_index=True)

data_test_scale  =  scaler.fit_transform(data_test)

x = []
y = []

for i in range(100, data_test_scale.shape[0]):
    x.append(data_test_scale[i-100:i])
    y.append(data_test_scale[i,0])
x, y = np.array(x), np.array(y)

y_predict = model.predict(x)

scale =1/scaler.scale_

y_predict = y_predict*scale

y = y*scale

plt.figure(figsize=(10,8))
plt.plot(y_predict, 'r', label = 'Predicted Price')
plt.plot(y, 'g', label = 'Original Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

last_100_days = data.Close.tail(100).values
last_100_days_scaled = scaler.transform(last_100_days.reshape(-1, 1))

future_days = 30
future_predictions = []
current_input = last_100_days_scaled

for _ in range(future_days):
    prediction = model.predict(current_input.reshape(1, 100, 1))
    future_predictions.append(prediction[0, 0])
    current_input = np.append(current_input[1:], prediction, axis=0)
    
future_predictions = scaler.inverse_transform(np.concatenate((last_100_days_scaled, np.array(future_predictions).reshape(-1, 1)), axis=0))[-future_days:]

plt.figure(figsize=(10,8))
plt.plot(data.Close, 'g', label='Historical Close Price')
plt.plot(range(len(data.Close), len(data.Close) + future_days), future_predictions, 'r', label='Future Predictions')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()