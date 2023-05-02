from flask import Flask, jsonify, request

from api.models import Id, Product, Order
from api.schemas import ProductSchema, IdSchema, OrderSchema
from api.db import Database

app = Flask(__name__)


@app.route('/products', methods=['GET'])
def get_products():
    name = request.args.get("name", default="", type=str)
    product_type = request.args.get("type", default="", type=str)
    status = request.args.get("status", default="", type=str)

    if name == "unknown":
        return '', 500

    schema = ProductSchema(many=True)
    return jsonify(schema.dump(Database.find_products(name, product_type, status)))


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    schema = ProductSchema()
    product = Database.find_product_by_id(product_id)
    if product:
        return jsonify(schema.dump(product))
    else:
        return jsonify({'error': 'Product not found'}), 404


@app.route('/products', methods=['POST'])
def add_product():
    product_request = ProductSchema().load(request.get_json())
    product = Product(product_request.get('name'), product_request.get('type'), product_request.get('inventory'))
    Database.add_product(product)
    schema = IdSchema()
    return jsonify(schema.dump(Id(product.id)))


@app.route('/products/<int:product_id>', methods=['POST'])
def update_product(product_id):
    product = Database.find_product_by_id(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    product_request = ProductSchema().load(request.get_json())
    Database.update_product(product_id, product_request)
    return '', 200


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Database.find_product_by_id(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    Database.delete_product(product_id)
    return '', 200


@app.route('/orders', methods=['GET'])
def get_orders():
    product_id = request.args.get("product_id", default="", type=int)
    status = request.args.get("status", default="", type=str)

    schema = OrderSchema(many=True)
    return jsonify(schema.dump(Database.find_orders(product_id, status)))


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    schema = OrderSchema()
    order = Database.find_order_by_id(order_id)
    if order:
        return jsonify(schema.dump(order))
    else:
        return jsonify({'error': 'Order not found'}), 404


@app.route('/orders', methods=['POST'])
def add_order():
    order_request = OrderSchema().load(request.get_json())
    product_id = order_request.get('productid')
    count = order_request.get('count')
    Database.reserve_product_inventory(product_id, count)
    order = Order(product_id, count, order_request.get('status'))
    Database.add_order(order)
    schema = IdSchema()
    return jsonify(schema.dump(Id(order.id)))


@app.route('/orders/<int:order_id>', methods=['POST'])
def update_order(order_id):
    order_request = OrderSchema().load(request.get_json())
    Database.update_order(order_request)
    return '', 200


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    Database.delete_order(order_id)
    return '', 200
