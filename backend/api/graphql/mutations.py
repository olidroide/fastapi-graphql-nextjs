import strawberry
from strawberry.types import Info

from .types import PersonType, FruitType


async def notify_new_flavour(data, name: str) -> PersonType:
    return await data.create_person(name=name)


# @strawberry.input
# class EatFruitInput:
#     person: PersonType
#     fruit: FruitType


@strawberry.type(description="Create/Update/Delete operations")
class Mutation:
    @strawberry.mutation
    async def add_person(self, name: str, info: Info) -> PersonType:
        # async with models.get_session() as s:
        #     db_author = None
        #     if author_name:
        #         sql = select(models.Author).where(models.Author.name == author_name)
        #         db_author = (await s.execute(sql)).scalars().first()
        #         if not db_author:
        #             return AuthorNotFound()
        #     else:
        #         return AuthorNameMissing()
        #     db_book = models.Book(name=name, author=db_author)
        #     s.add(db_book)
        #     await s.commit()
        # return
        return await info.context.data.create_person(name=name)

        # info.context.background_tasks.add_task(notify_new_flavour, info.context.data, name)
        # return True

    @strawberry.mutation
    async def remove_person(self, by_id: str, info: Info) -> PersonType:
        return await info.context.data.delete_person(by_id=by_id)

    @strawberry.mutation
    async def add_fruit(self, name: str, info: Info) -> FruitType:
        return await info.context.data.create_fruit(name=name)

    # @strawberry.mutation
    # async def eat_a_fruit(self, eat_fruit_input: EatFruitInput, info: Info) -> PersonType:
    #     print(eat_fruit_input)
    #     return eat_fruit_input.person
    #     # return await info.context.data.eat_fruit(person=person, fruit=fruit)
