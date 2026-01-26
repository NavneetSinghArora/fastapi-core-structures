from models import ProviderResponse
from fastapi import APIRouter
from constants import LLM_PROVIDERS

router = APIRouter()


@router.get("/providers/", response_model=list[ProviderResponse])
def get_providers(company: str = None) -> list[ProviderResponse]:
    if company:
        return [provider for provider in LLM_PROVIDERS if provider["name"] == company]
    return LLM_PROVIDERS
