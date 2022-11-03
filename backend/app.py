from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.graphql.router import FastAPIGraphQLRouter
from backend.data.provider import FakeData


def create_app():
    app = FastAPI()
    app.state.data = FakeData()

    fast_api_graphql_router = FastAPIGraphQLRouter(app)
    app.include_router(fast_api_graphql_router.get_router(),
                       prefix="/graphql", )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
