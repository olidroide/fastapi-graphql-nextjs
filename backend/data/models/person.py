from dataclasses import dataclass, field
from typing import Optional
from uuid import uuid4


def _default_factory_uuid() -> str:
    return str(uuid4())


# PYDANTIC USE CASE
# class _IdBaseModel(BaseModel):
#     id: str = Field(default_factory=_default_factory_uuid)
#
#     # def __hash__(self) -> int:
#     #     return self.id.__hash__()
#     # @property
#     # def id(self) -> str:
#     #     return str(self._id)
#
#
# class Person(_IdBaseModel):
#     name: str
#     surname: Optional[str]
#
#
# class Fruit(_IdBaseModel):
#     name: str
#     eaten_by: Optional[Person]


@dataclass
class IdBaseModel:
    id: str = field(default_factory=_default_factory_uuid)


@dataclass
class Person(IdBaseModel):
    name: str = ''
    surname: Optional[str] = None


@dataclass
class Fruit(IdBaseModel):
    name: str = ''
    eaten_by: Optional[Person] = None
    id: str = field(default_factory=_default_factory_uuid)
