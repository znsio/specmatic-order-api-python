from typing import TYPE_CHECKING

from flask import Blueprint, Response, abort, jsonify, request

from api.db import Database
from api.schemas import ProductSchema

if TYPE_CHECKING:
    from api.models import Product

products = Blueprint("products", __name__, url_prefix="/products")
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@products.route("/", methods=["GET"])
def get_products():
    name = request.args.get("name", default="", type=str)

    # NOTE: API Spec 500 Error when name is "unknown"
    if name == "unknown":
        return abort(500)

    args: Product = product_schema.load(request.args, partial=True)  # type: ignore[return-value]
    if not args.get("name") and not args.get("product_type"):
        return products_schema.dump(Database.all_products())

    return products_schema.dump(Database.find_products(args.get("name", ""), args.get("product_type")))


@products.route("/", methods=["POST"])
def add_product():
    product: Product = product_schema.load(request.json)  # type: ignore[return-value]
    Database.add_product(product)
    return jsonify(id=product["id"])


@products.route("/<int:id>", methods=["GET"])
def get_product(id: int):
    product = Database.find_product_by_id(id)
    if product:
        return product_schema.dump(product)
    return abort(404, "Product not found")


@products.route("/<int:id>", methods=["POST"])
def update_product(id: int):
    product = Database.find_product_by_id(id)
    if not product:
        return abort(404, "Product not found")
    new_data: Product = product_schema.load(request.json)  # type: ignore[return-value]
    Database.update_product(product, new_data)
    return Response("", 200, mimetype="text/plain")


@products.route("/<int:id>", methods=["DELETE"])
def delete_product(id: int):
    product = Database.find_product_by_id(id)
    if not product:
        return abort(404, "Product not found")
    Database.delete_product(id)
    return Response("", 200, mimetype="text/plain")
