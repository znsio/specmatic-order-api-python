from marshmallow import Schema, fields


class ProductSchema(Schema):
    name = fields.Str()
    type = fields.Str()
    inventory = fields.Int()
    id = fields.Int(default=0)


class OrderSchema(Schema):
    productid = fields.Int()
    count = fields.Int()
    status = fields.Str()
    id = fields.Int(default=0)


class IdSchema(Schema):
    id = fields.Int()
