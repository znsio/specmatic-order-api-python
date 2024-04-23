from api.db import Database
from api.models import Order

class OrderService:
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
    def update_order(order: Order):
        Database.update_order(order)