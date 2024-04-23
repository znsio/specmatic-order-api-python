from api.db import Database
from api.models import Product

class ProductService:
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
    def reserve_product_inventory(product_id: int, count: int):
        Database.reserve_product_inventory(product_id, count)