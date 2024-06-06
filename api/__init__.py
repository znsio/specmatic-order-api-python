from datetime import UTC, datetime

from flask import Flask, jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.errorhandler(ValidationError)
def handle_marshmallow_validation_error(e: "ValidationError"):
    return jsonify(
        timestamp=datetime.now(tz=UTC).isoformat(),
        status=400,
        error="Bad Request",
        message=",".join(e.messages),
    ), 400


@app.errorhandler(HTTPException)
def http_error_handler(e):
    return jsonify(
        timestamp=datetime.now(tz=UTC).isoformat(),
        status=e.code,
        error=e.name,
        message=e.description,
    ), e.code


from api.orders.routes import orders  # noqa: E402
from api.products.routes import products  # noqa: E402

app.register_blueprint(products)
app.register_blueprint(orders)
