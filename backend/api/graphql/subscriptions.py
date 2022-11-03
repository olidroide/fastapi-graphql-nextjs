import asyncio
from typing import AsyncGenerator

import strawberry
from strawberry.types import Info


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "world"


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, info: Info, target: int = 100) -> AsyncGenerator[int, None]:
        # print(info)
        info.context.data
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)
