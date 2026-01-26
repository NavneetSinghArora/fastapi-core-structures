from pydantic import BaseModel


class ProviderResponse(BaseModel):
    name: str
    models: list[str]
