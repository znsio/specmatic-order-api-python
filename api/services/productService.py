from api.db import Database
from api.models import Product

class ProductService:
    def find_products(self, name: str, product_type: str, status: str):
        return Database.find_products(name, product_type, status)

    def find_product_by_id(self, product_id: int):
        return Database.find_product_by_id(product_id)

    def delete_product(self, product_id: int):
        Database.delete_product(product_id)

    def add_product(self, product: Product):
        Database.add_product(product)

    def update_product(self, product_id: int, product: Product):
        Database.update_product(product_id, product)

    def inventory_status(self, product_id: int):
        return Database.inventory_status(product_id)

    def reserve_product_inventory(self, product_id: int, count: int):
        Database.reserve_product_inventory(product_id, count)