from typing import TYPE_CHECKING

from flask import Blueprint, Response, jsonify, request

from api.db import Database
from api.schemas import IdSchema, NewOrderSchema, OrderSchema

if TYPE_CHECKING:
    from api.models import Id, Order

orders = Blueprint("orders", __name__, url_prefix="/orders")
order_schema = OrderSchema()
new_order_schema = NewOrderSchema()
id_schema = IdSchema()


@orders.route("/", methods=["GET"])
def get_orders():
    productid = request.args.get("productid")
    if productid and productid.isdigit():
        productid = int(productid)

    data = request.args | {"productid": productid} if productid else {}
    args: Order = new_order_schema.load(data, partial=True)  # type: ignore[reportAssignmentType]
    if args.get("productid") is None and args.get("status") is None:
        return order_schema.dump(Database.all_orders(), many=True)

    return order_schema.dump(Database.find_orders(args.get("productid"), args.get("status")), many=True)


@orders.route("/", methods=["POST"])
def add_order():
    order: Order = new_order_schema.load(request.json)  # type: ignore[reportAssignmentType]
    Database.add_order(order)
    return jsonify(id=order["id"])


@orders.route("/<id>", methods=["GET"])
def get_order(id: str):  # noqa: A002
    params: Id = id_schema.load({"id": id})  # type: ignore[reportAssignmentType]
    order = Database.find_order_by_id_or_404(params["id"])
    return order_schema.dump(order)


@orders.route("/<id>", methods=["POST"])
def update_order(id: str):  # noqa: A002
    params: Id = id_schema.load({"id": id})  # type: ignore[reportAssignmentType]
    order = Database.find_order_by_id(params["id"])
    new_data: Order = order_schema.load(request.json)  # type: ignore[reportAssignmentType]
    if not order:
        # TODO: Temporary 200 Response AS per v3_SPEC, Needs fixing across Node and Python
        return Response("success", 200, mimetype="text/plain")
    Database.update_order(order, new_data)
    return Response("success", 200, mimetype="text/plain")


@orders.route("/<id>", methods=["DELETE"])
def delete_order(id: str):  # noqa: A002
    params: Id = id_schema.load({"id": id})  # type: ignore[reportAssignmentType]
    order = Database.find_order_by_id(params["id"])
    if not order:
        # TODO: Temporary 200 Response AS per v3_SPEC, Needs fixing across Node and Python
        return Response("success", 200, mimetype="text/plain")
    Database.delete_order(params["id"])
    return Response("success", 200, mimetype="text/plain")
