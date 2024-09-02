from dataclasses import dataclass
from typing import Any

from flask import abort
from werkzeug.datastructures import FileStorage

from api.schemas import ProductSchema, ProductType

product_schema = ProductSchema()
new_product_schema = ProductSchema(exclude=("id",))


@dataclass(slots=True, kw_only=True)
class Product:
    id: int
    name: str
    type: ProductType
    inventory: int

    @staticmethod
    def new_product(data: Any):
        data = new_product_schema.load(data)  # type: ignore[reportAssignmentType]
        return Product(**data, id=0)

    @staticmethod
    def validate_args(p_type: str | None):
        if not p_type:
            return None
        data: dict[str, ProductType] = new_product_schema.load({"type": p_type}, partial=True)  # type: ignore[reportAssignmentType]
        return data["type"]

    @staticmethod
    def validate_image(image: FileStorage | None):
        if not image:
            return abort(400, "No image was uploaded")
        return image

    @staticmethod
    def load(data: Any):
        data = product_schema.load(data)  # type: ignore[reportAssignmentType]
        return Product(**data)

    @staticmethod
    def dump(products: "list[Product] | Product", status_code: int = 200):
        return product_schema.dump(products, many=isinstance(products, list)), status_code
