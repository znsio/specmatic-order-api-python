from flask import Flask, jsonify, request, Response

from api import app
from api.models import Id, Product, Order
from api.schemas import ProductSchema, IdSchema, OrderSchema
from api.db import Database


@app.route('/products', methods=['GET'])
def get_products():
    name = request.args.get("name", default="", type=str)
    product_type = request.args.get("type", default="", type=str)
    status = request.args.get("status", default="", type=str)

    if name == "unknown":
        return Response('', 500, mimetype="application/json")

    schema = ProductSchema(many=True)
    return jsonify(schema.dump(Database.find_products(name, product_type, status)))


@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    schema = ProductSchema()
    product = Database.find_product_by_id(id)
    if product:
        return jsonify(schema.dump(product))
    else:
        return jsonify({'error': 'Product not found'}), 404


@app.route('/products', methods=['POST'])
def add_product():
    product:Product = ProductSchema().load(request.get_json())
    Database.add_product(product)
    schema = IdSchema()
    return jsonify(schema.dump(Id(product.id)))


@app.route('/products/<int:id>', methods=['POST'])
def update_product(id):
    product = Database.find_product_by_id(id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    product: Product = ProductSchema().load(request.get_json())
    Database.update_product(id, product)
    return Response('', 200, mimetype="text/plain")


@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Database.find_product_by_id(id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    Database.delete_product(id)
    return Response('', 200, mimetype="text/plain")


@app.route('/orders', methods=['GET'])
def get_orders():
    product_id = request.args.get("product_id", default="", type=int)
    status = request.args.get("status", default="", type=str)

    schema = OrderSchema(many=True)
    return jsonify(schema.dump(Database.find_orders(product_id, status)))


@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    schema = OrderSchema()
    order = Database.find_order_by_id(id)
    if order:
        return jsonify(schema.dump(order))
    else:
        return jsonify({'error': 'Order not found'}), 404


@app.route('/orders', methods=['POST'])
def add_order():
    order: Order = OrderSchema().load(request.get_json())
    Database.reserve_product_inventory(order.productid, order.count)
    Database.add_order(order)
    schema = IdSchema()
    return jsonify(schema.dump(Id(order.id)))


@app.route('/orders/<int:id>', methods=['POST'])
def update_order(id):
    order = OrderSchema().load(request.get_json())
    Database.update_order(order)
    return Response('', 200, mimetype="text/plain")


@app.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    Database.delete_order(id)
    return Response('', 200, mimetype="text/plain")
