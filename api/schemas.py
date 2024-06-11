import enum

from marshmallow import Schema, fields


class OrderStatus(str, enum.Enum):
    FULFILLED = "fulfilled"
    PENDING = "pending"
    CANCELLED = "cancelled"


class ProductType(str, enum.Enum):
    GADGET = "gadget"
    FOOD = "food"
    BOOK = "book"
    OTHER = "other"


class IdSchema(Schema):
    id = fields.Integer(required=True, strict=False)


class ProductSchema(IdSchema):
    name = fields.String(required=True)
    type = fields.Enum(ProductType, required=True, by_value=True)
    inventory = fields.Integer(required=True, strict=True)


class OrderSchema(IdSchema):
    productid = fields.Integer(required=True, strict=True)
    count = fields.Integer(required=True, strict=True)
    status = fields.Enum(OrderStatus, required=True, by_value=True)
