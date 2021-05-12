from flask import jsonify

from .fibonacci import get_fibonacci_sequence

cache = {"counter": 0}


def configure_routes(app):
    @app.route("/")
    def get():
        cache["counter"] = cache["counter"] + 1
        return jsonify(get_fibonacci_sequence(cache["counter"]))
