from typing import TYPE_CHECKING

from flask import Blueprint, Response, jsonify, request

from api.db import Database
from api.schemas import IdSchema, NewProductSchema, ProductSchema

if TYPE_CHECKING:
    from api.models import Id, Product

products = Blueprint("products", __name__, url_prefix="/products")
prod_schema = ProductSchema()
new_prod_schema = NewProductSchema()
id_schema = IdSchema()


@products.route("/", methods=["GET"])
def get_products():
    args: Product = prod_schema.load(request.args, partial=True)  # type: ignore[reportAssignmentType]

    if not args.get("name") and not args.get("product_type"):
        return prod_schema.dump(Database.all_products(), many=True)

    return prod_schema.dump(Database.find_products(args.get("name", ""), args.get("product_type")), many=True)


@products.route("/", methods=["POST"])
def add_product():
    product: Product = new_prod_schema.load(request.json)  # type: ignore[reportAssignmentType]
    Database.add_product(product)
    return jsonify(id=product["id"])


@products.route("<id>", methods=["GET"])
def get_product(id: str):  # noqa: A002
    params: Id = id_schema.load({"id": id})  # type: ignore[reportAssignmentType]
    product = Database.find_product_by_id_or_404(params["id"])
    return prod_schema.dump(product)


@products.route("<id>", methods=["POST"])
def update_product(id: str):  # noqa: A002
    params: Id = id_schema.load({"id": id})  # type: ignore[reportAssignmentType]
    new_data: Product = prod_schema.load(request.json)  # type: ignore[reportAssignmentType]
    product = Database.find_product_by_id(params["id"])
    if not product:
        # TODO: Temporary 200 Response AS per v3_SPEC, Needs fixing across Node and Python
        return Response("success", 200, mimetype="text/plain")
    Database.update_product(product, new_data)
    return Response("success", 200, mimetype="text/plain")


@products.route("<id>", methods=["DELETE"])
def delete_product(id: str):  # noqa: A002F
    params: Id = id_schema.load({"id": id})  # type: ignore[reportAssignmentType]
    product = Database.find_product_by_id(params["id"])
    if not product:
        # TODO: Temporary 200 Response AS per v3_SPEC, Needs fixing across Node and Python
        return Response("success", 200, mimetype="text/plain")
    Database.delete_product(params["id"])
    return Response("success", 200, mimetype="text/plain")
