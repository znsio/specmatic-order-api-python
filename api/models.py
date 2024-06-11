from dataclasses import dataclass

from api.schemas import IdSchema

id_schema = IdSchema()


@dataclass
class Id:
    id: int

    @staticmethod
    def load(id: int | str):  # noqa: A002
        data: dict = id_schema.load({"id": id})  # type: ignore[reportAssignmentType]
        return Id(**data)
