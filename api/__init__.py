from datetime import UTC, datetime

from flask import Flask, Response, jsonify, request
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.errorhandler(ValidationError)
def handle_marshmallow_validation_error(_: "ValidationError"):
    return jsonify(
        timestamp=datetime.now(tz=UTC).isoformat(),
        path=request.path,
        status=400,
        error="Bad Request",
    ), 400


@app.errorhandler(HTTPException)
def http_error_handler(e):
    # NOTE: API SPEC expects empty application/json response for 500
    if e.code == 500:
        return Response("", 500, mimetype="application/json")

    return jsonify(
        timestamp=datetime.now(tz=UTC).isoformat(),
        path=request.path,
        status=e.code,
        error=e.name,
    ), e.code


from api.orders.routes import orders  # noqa: E402
from api.products.routes import products  # noqa: E402

app.register_blueprint(products)
app.register_blueprint(orders)
