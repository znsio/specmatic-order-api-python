from api.db import Database
from api.models import Product, Order

class Service:
    @staticmethod
    def find_products(name: str, product_type: str, status: str):
        return Database.find_products(name, product_type, status)

    @staticmethod
    def find_product_by_id(product_id: int):
        return Database.find_product_by_id(product_id)

    @staticmethod
    def delete_product(product_id: int):
        Database.delete_product(product_id)

    @staticmethod
    def add_product(product: Product):
        Database.add_product(product)

    @staticmethod
    def update_product(product_id: int, product: Product):
        Database.update_product(product_id, product)

    @staticmethod
    def inventory_status(product_id: int):
        return Database.inventory_status(product_id)

    @staticmethod
    def find_orders(product_id: int, status: str):
        return Database.find_orders(product_id, status)

    @staticmethod
    def find_order_by_id(order_id: int):
        return Database.find_order_by_id(order_id)

    @staticmethod
    def delete_order(order_id: int):
        Database.delete_order(order_id)

    @staticmethod
    def add_order(order: Order):
        Database.add_order(order)

    @staticmethod
    def reserve_product_inventory(product_id: int, count: int):
        Database.reserve_product_inventory(product_id, count)

    @staticmethod
    def update_order(order: Order):
        Database.update_order(order)