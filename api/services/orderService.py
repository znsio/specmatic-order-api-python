from api.db import Database
from api.models import Order

class OrderService:
    def find_orders(self, product_id: int, status: str):
        return Database.find_orders(product_id, status)    

    def find_order_by_id(self, order_id: int):
        return Database.find_order_by_id(order_id)

    def delete_order(self, order_id: int):
        Database.delete_order(order_id)

    def add_order(self, order: Order):
        Database.add_order(order)

    def update_order(self, order: Order):
        Database.update_order(order)