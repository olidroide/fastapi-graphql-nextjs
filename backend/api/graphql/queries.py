from typing import List

import strawberry
from strawberry.types import Info

from backend.data.provider import DataProvider
from .types import PersonType, FruitType


async def load_persons(keys: List[str]) -> List[PersonType]:
    return [PersonType(id=key) for key in keys]


# custom_value: CustomContext = Depends(custom_context_dependency),
@strawberry.type(description="Read Operations")
class Query:
    @strawberry.field(description="Read all persons.")
    async def persons(self, info: Info) -> List[PersonType]:
        return [PersonType.from_data_class(person) for person in await info.context.data.get_persons()]

    @strawberry.field(description="Get a person from ID")
    async def get_person(self, info: Info, id: str) -> PersonType:
        person = await info.context.data.get_person(id)
        return PersonType.from_data_class(person)

    @strawberry.field(description="Read all fruits.")
    async def fruits(self, info: Info) -> List[FruitType]:
        all_data: DataProvider = info.context.data
        return [FruitType.from_data_class(fruit) for fruit in await all_data.get_fruits()]
