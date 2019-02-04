FROM python
LABEL authors="Nicolas Rey, Gabriel Nasr, Jorge Abreu"

WORKDIR /app

# Get GeoIP database
RUN wget https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz && \
    tar -xzvf GeoLite2-City.tar.gz  --strip-components 1 && \
    mv *.mmdb /app/geo.mmdb

COPY ./setup.py /app/setup.py
COPY ./src /app/src
RUN python3 setup.py install
COPY . /app

EXPOSE 5000/tcp
ENTRYPOINT ["python3"]
CMD ["main.py"]
