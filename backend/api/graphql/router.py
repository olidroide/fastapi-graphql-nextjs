from typing import ClassVar

from fastapi import APIRouter, FastAPI, Depends
from fastapi import WebSocket
from starlette.requests import Request
from strawberry.fastapi import GraphQLRouter, BaseContext
from strawberry.printer import print_schema

from .schema import get_schema
from backend.data.provider import DataProvider


# from starlette.websockets import WebSocket


class WebsocketHandler:

    def __init__(self, websocket: WebSocket = None):
        super().__init__()
        self.websocket = websocket

    async def handle_websocket(self):
        return self.websocket


class CustomContext(BaseContext):
    data: ClassVar[DataProvider] = None

    def __init__(self,
                 req: Request = None,
                 websocket_handler: WebsocketHandler = Depends()):
        super().__init__()
        self.request = req
        self.websocket = websocket_handler.websocket
        self._init_data_provider()

    def _init_data_provider(self):
        if self.request:
            self.data: DataProvider = self.request.app.state.data
            return

        if self.websocket:
            self.data: DataProvider = self.websocket.app.state.data
            return

        self.data = None

        # add a loader
        # self.person_loader: DataLoader = DataLoader(load_fn=load_persons)


# def custom_context_dependency(
#         req: Request = None,
#         # *args,
#         # request: Optional[Any] = None,
#         # background_tasks: Optional[BackgroundTasks] = None,
#         # response: Optional[Response] = None,
#         custom_context: CustomContext = Depends()
# ):
#     return CustomContext(
#         req=req,
#     )
#

async def get_context(
        custom_value: CustomContext = Depends(CustomContext),
) -> CustomContext:
    return custom_value


# async def get_context(
#         custom_value: CustomContext = Depends(custom_context_dependency),
# ) -> CustomContext:
#     return custom_value


class FastAPIGraphQLRouter:
    schema = None
    # graphql_app = None
    graphql_router = None

    def __init__(self, app: FastAPI) -> None:
        self._app = app
        self.schema = get_schema()

        self.graphql_router = GraphQLRouter(
            self.schema,
            context_getter=get_context,
            graphiql=True,
        )


    def get_router(self) -> APIRouter:
        with open('schema.graphql', 'w') as filehandle:
            filehandle.write(print_schema(self.schema))

        return self.graphql_router
