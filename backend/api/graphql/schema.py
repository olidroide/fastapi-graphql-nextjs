import strawberry

from .mutations import Mutation
from .queries import Query
from .subscriptions import Subscription


def get_schema() -> strawberry.Schema:
    return strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
