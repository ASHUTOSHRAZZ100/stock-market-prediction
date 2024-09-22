# Stock Price Prediction Web Application

This application provides users with insights into stock market trends through moving averages, historical stock data, and machine learning-driven price predictions. It’s a valuable tool for investors and business professionals looking to make data-driven decisions based on stock performance and future price forecasts.

## Key Features
- **Stock Data Visualization**: Analyze historical stock prices and trends using moving averages (e.g., 50-day, 100-day, and 200-day).
- **Machine Learning Predictions**: Predict stock prices using a trained Long Short-Term Memory (LSTM) model, giving insights into future stock behavior.
- **Future Forecasting**: Predict stock prices for the next 30 days based on past performance, helping users make informed business decisions.

## Target Audience
This tool is designed for:
- **Investors**: Who need real-time insights into stock trends and predictions.
- **Financial Analysts**: For data-driven stock analysis and future price forecasting.
- **Business Professionals**: Interested in market trends and economic insights.

## Installation and Setup

### Prerequisites
- **Python 3.x**
- **Virtual Environment** (optional but recommended)
- Install the required dependencies (see `requirements.txt`)

### Steps to Install
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/stock-prediction-app.git
   cd stock-prediction-app
   ```

2. **Create and Activate a Virtual Environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the LSTM Model**:
   - Place the pre-trained model (`Stock Predictions Model.keras`) in the project root directory.
   
5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the App**:
   - Open your browser and go to `http://127.0.0.1:5000/`.

## Project Structure
```
├── templates/               # HTML templates for the app
│   ├── home.html
│   ├── about.html
│   ├── team.html
│   ├── contact.html
│   ├── sign_in.html
│   ├── sign_up.html
│   └── graph.html
├── static/                  # Static files (CSS, images, etc.)
├── data.py                  # Helper functions for stock data processing
├── team.py                  # Content for the team and about pages
├── app.py                   # Main Flask app file
├── requirements.txt         # Python dependencies
├── Stock Predictions Model.keras # Trained LSTM model
└── README.md                # This file
```

## Use Cases
- **Stock Analysis**: Perform stock price analysis using technical indicators like moving averages, providing valuable insights for making buy/sell decisions.
- **Price Prediction**: Use machine learning to predict future stock movements and enhance business forecasting.
- **Future Planning**: Utilize 30-day forecasts for strategic financial planning, helping professionals anticipate market trends.

## Technologies Used
- **Flask**: For building the web application.
- **yfinance**: To fetch historical stock data.
- **pandas**: For data manipulation and analysis.
- **matplotlib**: For visualizing stock trends.
- **scikit-learn**: For scaling data.
- **keras** and **tensorflow**: To build and run the LSTM model for predictions.

## Running the Application
1. Navigate to the `/graph` route and input the stock ticker (e.g., "GOOG") along with a date range.
2. Visualize the stock's moving averages, compare predicted prices with actual prices, and get a future price forecast.

## Future Enhancements
- **Real-time Data Integration**: Incorporating real-time stock data feeds.
- **Portfolio Management**: Allowing users to analyze multiple stocks and build a personalized portfolio.
- **Advanced Analytics**: Offering additional technical indicators (e.g., RSI, Bollinger Bands).

## Contact Information
For more information or business inquiries, please reach out via the contact page of the application or directly email us at `business@stockpredictapp.com`.
