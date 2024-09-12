from flask import Flask,render_template,request,redirect,url_for
from sklearn.preprocessing import MinMaxScaler
import matplotlib
matplotlib.use('Agg')
from data import *

app = Flask(__name__)


model = load_model('Stock Predictions Model.keras') # set modal path

# root router
@app.route("/")
def home():
    return render_template("home.html")

# about router
@app.route("/about")
def about():
    return render_template("about.html")

# team router
@app.route("/team")
def team():
    return render_template("team.html")

# contact router
@app.route("/contact")
def contact():
    return render_template("contact.html")

# login router
@app.route("/login")
def login():
    return render_template("sign_in.html")

# register router
@app.route("/register")
def register():
    return render_template("sign_up.html")

# graph router
@app.route("/graph",methods=['GET','POST'])
def graph():
    if(request.method != 'GET'):
        stock = request.form.get('stock_ticker')
        start = request.form.get('start_date')
        end = request.form.get('end_date')
        
        # Fetch data
        try:
            data = yf.download(stock, start=start, end=end)
            data1 = data
            df = pd.DataFrame(data1)
            if data.empty:
                return "No data found for the stock symbol.", 404
        except Exception as e:
            return str(e), 500 
        # Data preparation
        data_train = pd.DataFrame(data.Close[0: int(len(data)*0.80)])
        data_test = pd.DataFrame(data.Close[int(len(data)*0.80): len(data)])
        scaler = MinMaxScaler(feature_range=(0,1)) 
        pas_100_days = data_train.tail(100)
        data_test = pd.concat([pas_100_days, data_test], ignore_index=True)
        data_test_scale = scaler.fit_transform(data_test)

    if (request.method == 'POST'):
        # Plot moving averages
        plots = {
            'ma50': plot_moving_average(data, 50),
            'ma50_ma100': plot_moving_averages(data, 50, 100),
            'ma100_ma200': plot_moving_averages(data, 100, 200),
            'original_vs_predicted': plot_original_vs_predicted(data, data_test_scale, scaler, model),
            'future_predictions': plot_future_predictions(data, scaler, model)
        }
        return render_template("graph.html", plots=plots, stock_data=df.to_dict('series'))
    if(request.method == "GET"):
        return redirect(url_for('home'))


# main
if __name__ == '__main__':
    app.run(debug=True)
    
