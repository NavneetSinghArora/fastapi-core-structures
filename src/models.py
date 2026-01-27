"""This module contains models for the application."""

from pydantic import BaseModel


class ProviderResponse(BaseModel):
    """This is a Pydantic model that represents a provider."""

    name: str
    models: list[str]
