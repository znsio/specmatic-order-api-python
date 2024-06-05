import enum
from typing import TypedDict


class ProductType(str, enum.Enum):
    GADGET = "gadget"
    FOOD = "food"
    BOOK = "book"
    OTHER = "other"

    def __str__(self):
        return self.value


class OrderStatus(str, enum.Enum):
    FULFILLED = "fulfilled"
    PENDING = "pending"
    CANCELLED = "cancelled"

    def __str__(self):
        return self.value


class Product(TypedDict):
    name: str
    product_type: ProductType
    inventory: int
    id: int


class Order(TypedDict):
    product_id: int
    count: int
    status: OrderStatus
    id: int
