import enum
from typing import TypedDict


class ProductType(str, enum.Enum):
    GADGET = "gadget"
    FOOD = "food"
    BOOK = "book"
    OTHER = "other"


class OrderStatus(str, enum.Enum):
    FULFILLED = "fulfilled"
    PENDING = "pending"
    CANCELLED = "cancelled"


class Id(TypedDict):
    id: int


class Product(Id):
    name: str
    type: ProductType
    inventory: int


class Order(Id):
    productid: int
    count: int
    status: OrderStatus
