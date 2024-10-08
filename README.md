# Stock Price Prediction Web Application

This web application allows users to visualize stock data, including historical prices, moving averages, predicted stock prices using a trained LSTM model, and future price predictions. The application is built using Flask and integrates with various data science and machine learning libraries such as `yfinance`, `pandas`, and `keras`.

## Features
- **Fetch Stock Data**: Users can input a stock ticker and a date range to fetch historical stock data.
- **Moving Averages**: Visualize 50-day, 100-day, and 200-day moving averages of the stock price.
- **Predicted vs. Actual Prices**: Compare actual stock prices to predicted prices using an LSTM model.
- **Future Price Predictions**: Forecast stock prices for the next 30 days based on historical data.
- **Team & About Pages**: Provides information about the project and the team members involved.
## Demo
### Home Page
![home](https://github.com/ASHUTOSHRAZZ100/stock-market-prediction/blob/main/static/img/redme/hero.png)
### Landing Page
![home](https://github.com/ASHUTOSHRAZZ100/stock-market-prediction/blob/main/static/img/redme/hero1.png)
### Sample Data
![home](https://github.com/ASHUTOSHRAZZ100/stock-market-prediction/blob/main/static/img/redme/data.png)
### Graph Data
![home](https://github.com/ASHUTOSHRAZZ100/stock-market-prediction/blob/main/static/img/redme/graph1.png)
![home](https://github.com/ASHUTOSHRAZZ100/stock-market-prediction/blob/main/static/img/redme/graph2.png)
## Installation

### Prerequisites
- Python
- Virtual environment (optional but recommended)
- Required Python packages (see `requirements.txt`)

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/stock-prediction-app.git
   cd stock-prediction-app
   ```

2. **Create a Virtual Environment (Optional):**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows use: venv\Scripts\activate
   ```

3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Pre-Trained Model:**
   - Ensure the pre-trained model (`Stock Predictions Model.keras`) is placed in the root directory of the project. If you do not have this file, you may need to train your own model or request access to the pre-trained model.

5. **Run the Application:**
   ```bash
   python app.py
   ```

6. **Access the Application:**
   - Open a browser and go to `http://127.0.0.1:5000/`.

## Project Structure
```
├── templates/               # HTML templates for the Flask app
│   ├── home.html
│   ├── about.html
│   ├── team.html
│   ├── contact.html
│   ├── sign_in.html
│   ├── sign_up.html
│   └── graph.html
├── static/                  # Static files (CSS, images, etc.)
├── data.py                  # Contains helper functions for data processing
├── team.py                  # Stores team member and about page content
├── app.py                   # Main Flask application file
├── requirements.txt         # Python dependencies
├── Stock Predictions Model.keras # Pre-trained LSTM model
└── README.md                # This file
```

## Usage
1. **Homepage**: Start at the home page where users can navigate to different sections (About, Team, Contact, Login, Register).
2. **Stock Graphs**:
   - Go to the graph section, enter a stock ticker (e.g., "GOOG"), and specify a date range to fetch stock data.
   - Visualize moving averages, predicted prices, and future price forecasts.
3. **About**: Learn more about the project.
4. **Team**: View details about the team members.

## Requirements
The required Python packages are listed in `requirements.txt`. Below are the main dependencies:
- `Flask`
- `yfinance`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `keras`
- `tensorflow`

To install these dependencies, simply run:

```bash
pip install -r requirements.txt
```
## Credits
This application was developed by **SHADOW** team.

### SHADOW Team
| ![Alok](https://res.cloudinary.com/dgflj5bqs/image/upload/f_auto,q_auto/v1/stock-prediction-team/bc4dk10zpypstd9vaykt) | ![Ashutosh](https://res.cloudinary.com/dgflj5bqs/image/upload/f_auto,q_auto/v1/stock-prediction-team/qz9w5yhkexzosngnhlc6) | ![Sayan](https://res.cloudinary.com/dgflj5bqs/image/upload/f_auto,q_auto/v1/stock-prediction-team/qigie3q3ajcvv2xwm50v) | ![Gaurav](https://res.cloudinary.com/dgflj5bqs/image/upload/f_auto,q_auto/v1/stock-prediction-team/hhu7lfwy5n23hpd7mwjz) |
| --- | --- | --- | --- |
| **Alok Raj** | **Ashutosh Raj** | **Sayan Singh** | **Gaurav Kumar** |
| Lead | Backend Developer | Machine Learning(ML) | User Interface(UI) Design |
| [LinkedIn](https://www.linkedin.com/in/alok-raj-4a6947202/)  [GitHub](https://github.com/Ar7pvt)  [Email](mailto:alokrajgrd8@gmail.com) | [LinkedIn](https://www.linkedin.com/in/ashutoshraj100/) [GitHub](https://github.com/ASHUTOSHRAZZ100) [Email](mailto:ashutoshrazz100@gmail.com) | [LinkedIn](https://www.linkedin.com/in/sayan-singh) [GitHub](https://github.com/FriendlyPedestal) [Email](mailto:thediscoverypost@gmail.com) | [LinkedIn](https://linkedin.com](https://www.linkedin.com/in/gaurav-kumar-199893227/)) [GitHub](https://github.com/iamgauravkr) [Email](mailto:gaurav14052003@gmail.com) |
| Final Year Undergraduate(CSE-AI) | Final Year Undergraduate(CSE-AI) | Final Year Undergraduate(CSE-AI) | Final Year Undergraduate(CSE-AI) |
