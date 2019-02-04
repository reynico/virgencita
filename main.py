from virgencita import app
import os

host = os.environ.get('APP_HOST', '127.0.0.1')
port = os.environ.get('APP_PORT', 5000)

if __name__ == '__main__':
    newApp = app.createApp()
    newApp.run(host, port)
