import os
import tempfile

import pytest

from flask import Flask
#from virgencita import createApp
from virgencita import app

@pytest.fixture
def appt():
    appt = app.createApp()
    appt.testing = True
    appt.app_context().push()
    yield appt


@pytest.fixture
def client(appt):
   return appt.test_client()

@pytest.fixture
def runner(appt):
    return appt.test_cli_runner()

def test_root(client):
    response = client.get('/')
    assert response.status_code == 200

def test_reply(client):
    response = client.get('/')
    assert response.data[0:6] == b"<head>"

def test_getApiKey():
    assert app.getApiKey() == "PUT_KEY"

def test_getAnalyticsKey():
    assert app.getAnalyticsKey() == "apikey"

def test_getLocation():
    lat = '-34.6037'
    lon = '-58.3816'
    assert app.getLocation('127.0.0.1') == (lat, lon)
