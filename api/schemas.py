from marshmallow import Schema, fields

from api.models import OrderStatus, ProductType


class NewProductSchema(Schema):
    name = fields.String(required=True)
    type = fields.Enum(ProductType, required=True, by_value=True)
    inventory = fields.Integer(required=True, strict=True)


class NewOrderSchema(Schema):
    productid = fields.Integer(required=True, strict=True)
    count = fields.Integer(required=True, strict=True)
    status = fields.Enum(OrderStatus, required=True, by_value=True)


class IdSchema(Schema):
    id = fields.Integer(required=True, strict=False)


class ProductSchema(NewProductSchema):
    id = fields.Integer(required=True, strict=True)


class OrderSchema(NewOrderSchema):
    id = fields.Integer(required=True, strict=True)
