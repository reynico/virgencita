# Virgencita del tiempo climático

[![Build Status](https://travis-ci.org/reynico/virgencita.svg?branch=master)](https://travis-ci.org/reynico/virgencita)

### Setup
- Download [GeoIP city location database](https://dev.maxmind.com/geoip/geoip2/geolite2/)
- Uncompress and rename to `geo.mmdb`
- Set your `FORECAST_API_KEY_1`. Create an account at [DarkSky](https://darksky.net/)
- Set your `FORECAST_ANALYTICS_KEY` to have metrics at Google Analytics
- Install the Python requirements `pip3 install -r requirements.txt`
- Run with `python3 app.py`

### How to test locally
Requires 18.02.0+
- Edit `docker-compose.yml` with your keys
```
docker-compose build
docker-compose up
```
