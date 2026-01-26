from fastapi import APIRouter

router = APIRouter()


@router.get("/providers/")
def get_providers(provider_name: str = None) -> dict | list:
    providers = {
        "AI Providers": ["OpenAI", "Google", "Anthropic", "Cohere", "HuggingFace"]
    }
    if provider_name is None:
        return providers
    if provider_name not in providers["AI Providers"]:
        return {"error": f"Provider {provider_name} not found"}
    return {"AI Provider": provider_name}
