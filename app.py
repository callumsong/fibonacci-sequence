from flask import Flask
from handlers.routes import configure_routes

import logging

logging.basicConfig(
    filename="app.log",
    filemode="w",
    format="%(asctime)s - %(message)s",
    level=logging.INFO,
)

app = Flask(__name__)

configure_routes(app)

if __name__ == "__main__":
    app.run()
