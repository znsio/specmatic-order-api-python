from itertools import count
from typing import ClassVar

from api.models import Order, OrderStatus, Product, ProductType


class Database:
    _products: ClassVar[dict[int, Product]] = {
        10: Product(name="XYZ Phone", product_type=ProductType.GADGET, inventory=10, id=10),
        20: Product(name="Gemini", product_type=ProductType.OTHER, inventory=10, id=20),
    }

    _orders: ClassVar[dict[int, Order]] = {
        10: Order(product_id=10, count=2, status=OrderStatus.PENDING, id=10),
        20: Order(product_id=10, count=1, status=OrderStatus.PENDING, id=20),
    }

    product_iter = count((max(_products) + 1) if _products else 1)
    order_iter = count((max(_orders) + 1) if _orders else 1)

    @staticmethod
    def all_products():
        return Database._products.values()

    @staticmethod
    def find_products(name: str, product_type: ProductType | None):
        return [
            product
            for product in Database._products.values()
            if product["name"].lower() == name.lower() or product["product_type"] == product_type
        ]

    @staticmethod
    def find_product_by_id(product_id: int):
        return Database._products.get(product_id)

    @staticmethod
    def delete_product(product_id: int):
        if Database._products.get(product_id):
            del Database._products[product_id]

    @staticmethod
    def add_product(product: Product):
        product["id"] = next(Database.product_iter)
        Database._products[product["id"]] = product

    @staticmethod
    def update_product(product: Product, new_data: Product):
        product["name"] = new_data["name"]
        product["product_type"] = new_data["product_type"]
        product["inventory"] = new_data["inventory"]

    @staticmethod
    def all_orders():
        return Database._orders.values()

    @staticmethod
    def find_orders(product_id: int, status: OrderStatus | None):
        return [
            order
            for order in Database._orders.values()
            if order["product_id"] == product_id or order["status"] == status
        ]

    @staticmethod
    def find_order_by_id(order_id: int):
        return Database._orders.get(order_id)

    @staticmethod
    def delete_order(order_id: int):
        if Database._orders.get(order_id):
            del Database._orders[order_id]

    @staticmethod
    def add_order(order: Order):
        order["id"] = next(Database.order_iter)
        Database._orders[order["id"]] = order

    @staticmethod
    def update_order(order: Order, new_data: Order):
        order["product_id"] = new_data["product_id"]
        order["count"] = new_data["count"]
        order["status"] = new_data["status"]
