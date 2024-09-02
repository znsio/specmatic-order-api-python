import pathlib
from itertools import count
from typing import ClassVar

from flask import abort
from werkzeug.datastructures import FileStorage

from api import app
from api.orders.models import Order, OrderStatus
from api.products.models import Product, ProductType


class Database:
    _products: ClassVar[dict[int, Product]] = {
        10: Product(name="XYZ Phone", type=ProductType.GADGET, inventory=10, id=10),
        20: Product(name="Gemini", type=ProductType.OTHER, inventory=10, id=20),
    }

    _product_images: ClassVar[dict[int, list[str]]] = {
        10: ["https://picsum.photos/id/0/5000/3333"],
        20: ["https://picsum.photos/id/0/5000/3333"],
    }

    _orders: ClassVar[dict[int, Order]] = {
        10: Order(productid=10, count=2, status=OrderStatus.PENDING, id=10),
        20: Order(productid=10, count=1, status=OrderStatus.PENDING, id=20),
    }

    product_iter = count((max(_products) + 1) if _products else 1)
    order_iter = count((max(_orders) + 1) if _orders else 1)

    @staticmethod
    def save_image(image: FileStorage, fallback_filename: str) -> str:
        file_name = image.filename or fallback_filename
        save_path = pathlib.Path(app.config["UPLOAD_FOLDER"]) / file_name
        image.save(save_path)
        return str(save_path)

    @staticmethod
    def all_products():
        return list(Database._products.values())

    @staticmethod
    def get_product_by_id(product_id: int):
        return Database._products.get(product_id)

    @staticmethod
    def get_product_by_id_or_404(product_id: int):
        product = Database._products.get(product_id)
        if not product:
            abort(404, f"Product with ID {product_id} was not found")
        return product

    @staticmethod
    def search_products(product_type: ProductType | None):
        if not product_type:
            return Database.all_products()
        return [product for product in Database._products.values() if product.type == product_type]

    @staticmethod
    def add_product(product: Product):
        product.id = next(Database.product_iter)
        Database._products[product.id] = product
        return product

    @staticmethod
    def update_product(product: Product, new_data: Product):
        product.name = new_data.name
        product.type = new_data.type
        product.inventory = new_data.inventory

    @staticmethod
    def get_product_images(product: Product) -> list[str]:
        return Database._product_images.get(product.id, [])

    @staticmethod
    def update_product_image(product: Product, new_image: FileStorage):
        save_path = Database.save_image(new_image, fallback_filename=f"{product.id}.png")
        if not Database._product_images.get(product.id):
            Database._product_images[product.id] = []
        Database._product_images[product.id].append(save_path)

    @staticmethod
    def delete_product(product: Product):
        if Database._products.get(product.id):
            del Database._products[product.id]

    @staticmethod
    def all_orders():
        return Database._orders.values()

    @staticmethod
    def get_order_by_id(order_id: int):
        return Database._orders.get(order_id)

    @staticmethod
    def get_order_by_id_or_404(order_id: int):
        order = Database._orders.get(order_id)
        if not order:
            abort(404, f"Order with ID {order_id} was not found")
        return order

    @staticmethod
    def __order_filter(order: Order, product_id: int | None, status: OrderStatus | None):
        return (not product_id or order.productid == product_id) and (not status or order.status == status)

    @staticmethod
    def search_orders(product_id: int | None, status: OrderStatus | None):
        return [order for order in Database._orders.values() if Database.__order_filter(order, product_id, status)]

    @staticmethod
    def add_order(order: Order):
        order.id = next(Database.order_iter)
        Database._orders[order.id] = order
        return order

    @staticmethod
    def update_order(order: Order, new_data: Order):
        order.productid = new_data.productid
        order.count = new_data.count
        order.status = new_data.status

    @staticmethod
    def delete_order(order: Order):
        if Database._orders.get(order.id):
            del Database._orders[order.id]
