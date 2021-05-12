from flask import jsonify
import logging

from .fibonacci import get_fibonacci_sequence

cache = {"counter": 0, "skipped_counter": False}


def configure_routes(app):
    @app.route("/")
    def fibonacci():
        logging.info("Counter is " + str(cache["counter"]))
        cache["counter"] = cache["counter"] + 1
        return jsonify(get_fibonacci_sequence(cache["counter"]))
