from flask import Flask, render_template, request, url_for
from forecastiopy import *
import geoip2.database
import random
import os


def create_app():

    app = Flask(__name__)
    reader = geoip2.database.Reader('geo.mmdb')

    @app.route('/')
    def show_index():
        client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        apiKey = random.sample(set([os.environ['FORECAST_API_KEY_1'], os.environ['FORECAST_API_KEY_2'], os.environ['FORECAST_API_KEY_3']]), 1)
        try:
            client_response = reader.city(client_ip)
            lat = str(client_response.location.latitude)
            lon = str(client_response.location.longitude)
        except:
            lat = '-34.6037'
            lon = '-58.3816'
            pass
        fio = ForecastIO.ForecastIO(apiKey[0], latitude=lat, longitude=lon)
        current = FIOCurrently.FIOCurrently(fio)
        return render_template("index.html", probabilidad = int(current.humidity*100))
    return app
