from forecastiopy import *
from flask import Flask, render_template, request, url_for
import os
app = Flask(__name__)
Buenos_Aires = [-34.6037, -58.3816]

@app.route('/')
def show_index():
    apiKey = os.environ['FORECAST_API_KEY']
    fio = ForecastIO.ForecastIO(apiKey, latitude=Buenos_Aires[0], longitude=Buenos_Aires[1])
    current = FIOCurrently.FIOCurrently(fio)
    return render_template("index.html", probabilidad = int(current.precipProbability*100))

if __name__ == '__main__':
    app.run()
