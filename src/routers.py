"""This is a FastAPI router that provides a list of LLM providers."""

from models import ProviderResponse
from fastapi import APIRouter
from constants import LLM_PROVIDERS

router = APIRouter()


@router.get("/providers/", response_model=list[ProviderResponse])
def get_providers(company: str = None) -> list[ProviderResponse]:
    """This is a FastAPI endpoint that returns a list of LLM providers.

    This endpoint utilizes the Pydantic model to validate the response.

    Args:
        company (str, optional): The name of the company to filter by. Defaults to None.

    Returns:
        list[ProviderResponse]: A list of LLM providers.
    """
    if company:
        return [provider for provider in LLM_PROVIDERS if provider["name"] == company]
    return LLM_PROVIDERS
