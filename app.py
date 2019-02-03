from flask import Flask, render_template, request, url_for
import sys
import requests
import requests_cache
import geoip2.database
import logging
import random
import os

host = os.environ.get('APP_HOST', '127.0.0.1')
port = os.environ.get('APP_PORT', 5000)

requests_cache.install_cache('virgencita', expire_after=1800)

reader = geoip2.database.Reader('geo.mmdb')


def getLocation(client_ip):
    try:
        client_response = reader.city(client_ip)
        lat = str(round(client_response.location.latitude, 2))
        lon = str(round(client_response.location.longitude, 2))
    except:
        lat = '-34.6037'
        lon = '-58.3816'
        pass
    print('Lat/Lon: ' + lat + ', ' + lon, file=sys.stdout)
    sys.stdout.flush()
    return(lat, lon)


def getCity(client_ip):
    try:
        client_response = reader.city(client_ip)
        city = str(client_response.city.name)
    except:
        city = 'Buenos Aires'
        pass
    print('City: ' + city, file=sys.stdout)
    sys.stdout.flush()
    return(city)


def getApiKey():
    return(os.environ['FORECAST_API_KEY_1'])


def getAnalyticsKey():
    return(os.environ['FORECAST_ANALYTICS_KEY'])


def getForecast(client_ip):
    coords = getLocation(client_ip)
    r = requests.get('https://api.darksky.net/forecast/%s/%s,%s' %
                     (getApiKey(), coords[0], coords[1]))
    print('Is cached: ' + str(r.from_cache) + '\n', file=sys.stdout)
    sys.stdout.flush()
    data = r.json()
    return(data)


def getHumidity(forecast):
    humidity = int(forecast['currently']['humidity']*100)
    precipP = int(forecast['currently']['precipProbability']*100)
    return((humidity+precipP)/2)

app = Flask(__name__)


app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True


@app.route('/')
def show_index():
    client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    print('Client IP: ' + str(client_ip), file=sys.stdout)
    sys.stdout.flush()
    forecast = getForecast(client_ip)
    return render_template("index.html", analytics_id=getAnalyticsKey(),
                           probability=getHumidity(forecast),
                           geocity=getCity(client_ip))

if __name__ == '__main__':
    app.run(host, port)
