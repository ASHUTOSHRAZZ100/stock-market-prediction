import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
import matplotlib.pyplot as plt
import io
import base64


def plot_moving_average(data, window):
    plt.figure(figsize=(8, 6))
    ma = data['Close'].rolling(window).mean()
    plt.plot(data.index, ma, 'r', label=f'MA{window}')
    plt.plot(data.index, data['Close'], 'g', label='Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    return save_plot()

def plot_moving_averages(data, ma1, ma2):
    plt.figure(figsize=(8, 6))
    ma1_days = data['Close'].rolling(ma1).mean()
    ma2_days = data['Close'].rolling(ma2).mean()
    plt.plot(data.index, ma1_days, 'r', label=f'MA{ma1}')
    plt.plot(data.index, ma2_days, 'b', label=f'MA{ma2}')
    plt.plot(data.index, data['Close'], 'g', label='Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    return save_plot()

def plot_original_vs_predicted(data, data_test_scale, scaler, model):
    x = []
    y = []
    for i in range(100, data_test_scale.shape[0]):
        x.append(data_test_scale[i-100:i])
        y.append(data_test_scale[i, 0])
    x, y = np.array(x), np.array(y)
    predict = model.predict(x)
    scale = 1 / scaler.scale_
    predict = predict * scale
    y = y * scale
    plt.figure(figsize=(8, 6))
    plt.plot(predict, 'r', label='Predicted Price')
    plt.plot(y, 'g', label='Original Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    return save_plot()

def plot_future_predictions(data, scaler, model):
    last_100_days = data.Close.tail(100).values
    last_100_days_scaled = scaler.transform(last_100_days.reshape(-1, 1))

    future_days = 30
    future_predictions = []
    current_input = last_100_days_scaled

    for _ in range(future_days):
        prediction = model.predict(current_input.reshape(1, 100, 1))
        future_predictions.append(prediction[0, 0])
        current_input = np.append(current_input[1:], prediction, axis=0)

    future_predictions = scaler.inverse_transform(
        np.concatenate((last_100_days_scaled, np.array(future_predictions).reshape(-1, 1)), axis=0)
    )[-future_days:]

    future_dates = pd.date_range(start=data.index[-1] + pd.DateOffset(1), periods=future_days)

    plt.figure(figsize=(12, 8))
    plt.plot(data.index, data['Close'], 'g', label='Historical Close Price')
    plt.plot(future_dates, future_predictions, 'r', label='Future Predictions')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    return save_plot()

def save_plot():
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return base64.b64encode(img.getvalue()).decode('utf-8')
