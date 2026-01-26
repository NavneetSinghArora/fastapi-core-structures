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
        return {
            "success": False,
            "message": f"Provider {provider_name} is not available",
        }
    return {"success": True, "message": f"Provider {provider_name} is available"}
