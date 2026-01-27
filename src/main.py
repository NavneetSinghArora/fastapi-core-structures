"""This is a FastAPI application that aims to provide a capability to call a bunch of LLM providers."""

from fastapi import FastAPI

import routers

app = FastAPI()

app.include_router(routers.router)


@app.get("/")
def read_root() -> dict[str, str]:
    """This is the root endpoint that returns a simple message."""
    return {"Hello": "World"}
