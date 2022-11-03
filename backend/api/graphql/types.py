from typing import Optional, TypeVar, Generic

import strawberry

from backend.data.models.person import Person, Fruit, IdBaseModel

_InputDataClassMapper = TypeVar("_InputDataClassMapper", bound=IdBaseModel)


class BaseType(Generic[_InputDataClassMapper]):
    @classmethod
    def from_data_class(cls, input_data_class: Optional[_InputDataClassMapper] = None):
        return cls(**input_data_class.__dict__) if input_data_class else None


@strawberry.type
class PersonType(BaseType, Person):
    ...


@strawberry.type
class FruitType(BaseType, Fruit):
    eaten_by: Optional[PersonType] = None
