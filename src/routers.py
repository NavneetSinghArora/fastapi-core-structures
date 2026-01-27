"""This is a FastAPI router that provides a list of LLM providers."""

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from models import ProviderResponse
from constants import LLM_PROVIDERS
from database.main import get_database_connection
from database.models import Users

router = APIRouter()


@router.get("/providers/", response_model=list[ProviderResponse])
def get_providers(company: str | None = None) -> list[ProviderResponse]:
    """This is a FastAPI endpoint that returns a list of LLM providers.

    This endpoint utilizes the Pydantic model to validate the response.

    Args:
        company (str, optional): The name of the company to filter by. Defaults to None.

    Returns:
        list[ProviderResponse]: A list of LLM providers.
    """
    if company:
        return [ProviderResponse(**provider) for provider in LLM_PROVIDERS if provider["name"] == company]
    return [ProviderResponse(**provider) for provider in LLM_PROVIDERS]


@router.get("/users")
def get_users(connection: Session = Depends(get_database_connection)) -> list:
    """This is a FastAPI endpoint that returns a list of users."""
    return connection.query(Users).all()
