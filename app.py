from flask import Flask, render_template, request, url_for
import sys
import requests
import requests_cache
import geoip2.database
import random
import os

requests_cache.install_cache('virgencita', expire_after=1800)


def getLocation(client_ip):
    reader = geoip2.database.Reader('geo.mmdb')
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


def getApiKey():
    return(os.environ['FORECAST_API_KEY_1'])


def getHumidity(client_ip):
    coords = getLocation(client_ip)
    r = requests.get('https://api.darksky.net/forecast/%s/%s,%s' %
                     (getApiKey(), coords[0], coords[1]))
    print('Is cached: ' + str(r.from_cache), file=sys.stdout)
    sys.stdout.flush()
    data = r.json()
    return(int(data['currently']['humidity']*100))

app = Flask(__name__)


@app.route('/')
def show_index():
    client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    print('Client IP: ' + str(client_ip), file=sys.stdout)
    sys.stdout.flush()
    return render_template("index.html", probabilidad=getHumidity(client_ip))

if __name__ == '__main__':
    app.run()
