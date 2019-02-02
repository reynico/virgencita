import os
import tempfile

import pytest

from flask import Flask
from virgencita import create_app

@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    app.app_context().push()
    yield app


@pytest.fixture
def client(app):
   return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_root(client):
    response = client.get('/')
    assert response.status_code == 200

def test_reply(client):
    response = client.get('/')
    assert response.data[0:6] == b"<head>"
