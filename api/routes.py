from flask import jsonify, request, Response
from marshmallow import ValidationError

from api import app
from api.models import Id, Product, Order
from api.schemas import ProductSchema, IdSchema, OrderSchema
from api.services.productService import ProductService
from api.services.orderService import OrderService

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({
        "timestamp": '',
        'status': 400,
        'error': '',
        'message': 'Marshmallow validation error'
    }), 400
    
@app.errorhandler(404)
def handle_404_error(error):
    return jsonify({
        "timestamp": '',
        'status': 400,
        'error': '',
        'message': 'Invalid path parameter'
    }), 400

@app.route('/products', methods=['GET'])
def get_products():
    name = request.args.get("name", type=str)
    product_type = request.args.get("type", type=str)
    status = request.args.get("status", type=str)

    if name == "unknown":
        return Response('', 500, mimetype="application/json")
    
    if product_type is not None and product_type not in ['gadget', 'book', 'food', 'other']:
        return jsonify({'error': 'Invalid product type'}), 400

    schema = ProductSchema(many=True)
    return jsonify(schema.dump(ProductService.find_products(name, product_type, status)))


@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    schema = ProductSchema()
    product = ProductService.find_product_by_id(id)
    if product:
        return jsonify(schema.dump(product))
    else:
        return jsonify({'error': 'Product not found'}), 404


@app.route('/products', methods=['POST'])
def add_product():
    product:Product = ProductSchema().load(request.get_json())
    ProductService.add_product(product)
    schema = IdSchema()
    return jsonify(schema.dump(Id(product.id)))


@app.route('/products/<int:id>', methods=['POST'])
def update_product(id):
    product = ProductService.find_product_by_id(id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    product: Product = ProductSchema().load(request.get_json())
    ProductService.update_product(id, product)
    return Response('', 200, mimetype="text/plain")


@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = ProductService.find_product_by_id(id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    ProductService.delete_product(id)
    return Response('', 200, mimetype="text/plain")


@app.route('/orders', methods=['GET'])
def get_orders():
    product_id = request.args.get("productid")
    if product_id is not None:
        try: 
             val = int(product_id)
        except ValueError:
            return jsonify({'error': 'Invalid path parameter'}), 400
    
    status = request.args.get("status", type=str)

    schema = OrderSchema(many=True)
    return jsonify(schema.dump(OrderService.find_orders(product_id, status)))


@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    schema = OrderSchema()
    order = OrderService.find_order_by_id(id)
    if order:
        return jsonify(schema.dump(order))
    else:
        return jsonify({'error': 'Order not found'}), 404


@app.route('/orders', methods=['POST'])
def add_order():
    order: Order = OrderSchema().load(request.get_json())
    ProductService.reserve_product_inventory(order.productid, order.count)
    OrderService.add_order(order)
    schema = IdSchema()
    return jsonify(schema.dump(Id(order.id)))


@app.route('/orders/<int:id>', methods=['POST'])
def update_order(id):
    order = OrderSchema().load(request.get_json())
    OrderService.update_order(order)
    return Response('', 200, mimetype="text/plain")


@app.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    OrderService.delete_order(id)
    return Response('', 200, mimetype="text/plain")
