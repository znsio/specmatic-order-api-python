from dataclasses import dataclass
from typing import Any

from api.schemas import OrderSchema, OrderStatus

order_schema = OrderSchema()
new_order_schema = OrderSchema(exclude=("id",))


@dataclass(slots=True, kw_only=True)
class Order:
    id: int
    productid: int
    count: int
    status: OrderStatus = OrderStatus.PENDING

    @staticmethod
    def new_order(data: Any):
        data = new_order_schema.load(data)  # type: ignore[reportAssignmentType]
        return Order(**data, id=0)

    @staticmethod
    def validate_args(product_id: Any | None, status: str | None) -> tuple[int | None, OrderStatus | None]:
        args = {}

        if product_id:
            args["productid"] = int(product_id) if product_id.isdigit() else product_id

        if status:
            args["status"] = status

        data: dict = new_order_schema.load(args, partial=True)  # type: ignore[reportAssignmentType]
        return data.get("productid"), data.get("status")

    @staticmethod
    def load(data: Any):
        data = order_schema.load(data)  # type: ignore[reportAssignmentType]
        return Order(**data)

    @staticmethod
    def dump(products: "list[Order] | Order", status_code: int = 200):
        return order_schema.dump(products, many=isinstance(products, list)), status_code
