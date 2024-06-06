from marshmallow import Schema, fields, post_load, validate

from api.models import Order, OrderStatus, Product, ProductType

VALID_PRODUCT_TYPES = [t.value for t in ProductType]
VALID_ORDER_STATUS = [s.value for s in OrderStatus]


class ProductSchema(Schema):
    id = fields.Integer(required=False, load_default=None)
    name = fields.String(required=True)
    product_type = fields.String(required=True, validate=validate.OneOf(VALID_PRODUCT_TYPES), data_key="type")
    inventory = fields.Integer(required=True)

    @post_load
    def serialize_enum(self, data: Product, **_):
        if data.get("product_type"):
            data["product_type"] = ProductType(data["product_type"])
        return data


class OrderSchema(Schema):
    id = fields.Integer(required=False, load_default=None)
    product_id = fields.Integer(required=True, data_key="productid")
    count = fields.Integer(required=True)
    status = fields.String(required=True, validate=validate.OneOf(VALID_ORDER_STATUS))

    @post_load
    def serialize_enum(self, data: Order, **_):
        if data.get("status"):
            data["status"] = OrderStatus(data["status"])
        return data
