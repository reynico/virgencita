FROM ubuntu:18.04
LABEL authors="Nicolas Rey, Gabriel Nasr, Jorge Abreu"

WORKDIR /app
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev wget

# Get GeoIP database
RUN wget https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz && \
    tar -xzvf GeoLite2-City.tar.gz  --strip-components 1 && \
    mv *.mmdb /app/geo.mmdb

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt
COPY . /app

EXPOSE 5000/tcp
ENTRYPOINT ["python3"]
CMD ["app.py"]
