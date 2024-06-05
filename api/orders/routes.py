from typing import TYPE_CHECKING

from flask import Blueprint, Response, abort, jsonify, request

from api.db import Database
from api.schemas import OrderSchema

if TYPE_CHECKING:
    from api.models import Order

orders = Blueprint("orders", __name__, url_prefix="/orders")
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)


@orders.route("/", methods=["GET"])
def get_orders():
    args: Order = order_schema.load(request.args, partial=True)  # type: ignore[return-value]

    if not args.get("product_id") and not args.get("status"):
        return orders_schema.dump(Database.all_orders())

    return orders_schema.dump(Database.find_orders(args.get("product_id", 0), args.get("status")))


@orders.route("/", methods=["POST"])
def add_order():
    order: Order = order_schema.load(request.json)  # type: ignore[return-value]
    Database.add_order(order)
    return jsonify(id=order["id"])


@orders.route("/<int:id>", methods=["GET"])
def get_order(id: int):
    order = Database.find_order_by_id(id)
    if order:
        return order_schema.dump(order)
    return abort(404, "Order not found")


@orders.route("/<int:id>", methods=["POST"])
def update_order(id: int):
    order = Database.find_order_by_id(id)
    if not order:
        return abort(404, "Order not found")
    new_data: Order = order_schema.load(request.json)  # type: ignore[return-value]
    Database.update_order(order, new_data)
    return Response("", 200, mimetype="text/plain")


@orders.route("/<int:id>", methods=["DELETE"])
def delete_order(id: int):
    order = Database.find_order_by_id(id)
    if not order:
        return abort(404, "Order not found")
    Database.delete_order(id)
    return Response("", 200, mimetype="text/plain")
