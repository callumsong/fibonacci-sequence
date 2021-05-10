from flask import jsonify

cache = {}


def get_fibonacci_sequence():
    if not ("latest" in cache):
        cache["previous"] = 0
        cache["latest"] = 0
        cache["counter"] = 0
    elif cache["latest"] == 0:
        cache["previous"] = 1
    new_latest = cache["previous"] + cache["latest"]
    new_previous = cache["latest"]

    cache["latest"] = new_latest
    cache["previous"] = new_previous
    cache["counter"] = cache["counter"] + 1
    return {"value": new_latest, "counter": cache["counter"]}


def configure_routes(app):
    @app.route("/")
    def get():

        return jsonify(get_fibonacci_sequence())
