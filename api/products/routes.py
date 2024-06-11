from flask import Blueprint, Response, jsonify, request

from api.db import Database
from api.models import Id
from api.products.models import Product

products = Blueprint("products", __name__, url_prefix="/products")


@products.route("/", methods=["GET"])
def get_products():
    p_type = Product.validate_args(request.args.get("type"))
    return Product.dump(Database.search_products(p_type))


@products.route("/", methods=["POST"])
def add_product():
    product: Product = Product.new_product(request.json)
    product = Database.add_product(product)
    return jsonify(id=product.id)


@products.route("<id>", methods=["GET"])
def get_product(id: str):  # noqa: A002
    params: Id = Id.load(id)
    product = Database.get_product_by_id_or_404(params.id)
    return Product.dump(product)


@products.route("<id>", methods=["POST"])
def update_product(id: str):  # noqa: A002
    params: Id = Id.load(id)
    product = Database.get_product_by_id_or_404(params.id)
    new_data: Product = Product.load(request.json)
    Database.update_product(product, new_data)
    return Response("success", 200, mimetype="text/plain")


@products.route("<id>", methods=["DELETE"])
def delete_product(id: str):  # noqa: A002F
    params: Id = Id.load(id)
    product = Database.get_product_by_id_or_404(params.id)
    Database.delete_product(product)
    return Response("success", 200, mimetype="text/plain")
