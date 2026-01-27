"""This module contains constants for the application."""

LLM_PROVIDERS = [
    {
        "name": "OpenAI",
        "description": "OpenAI is a research organization focused on developing and advancing AI technology.",
        "url": "https://openai.com",
        "models": ["gpt-3.5-turbo", "gpt-4", "gpt-4o", "gpt-4o-mini"],
    },
    {
        "name": "Google",
        "description": "Google is a search engine company that provides a wide range of products and services.",
        "url": "https://google.com",
        "models": [
            "gemini-1.5-flash",
            "gemini-2.0-flash-exp",
            "gemini-2.0-flash-128k-exp",
        ],
    },
    {
        "name": "Anthropic",
        "description": "Anthropic is a research organization focused on developing and advancing AI technology.",
        "url": "https://anthropic.com",
        "models": [
            "claude-3-5-sonnet",
            "claude-3-5-haiku",
            "claude-3-5-sonnet-20240620",
            "claude-3-5-haiku-20240620",
        ],
    },
    {
        "name": "Cohere",
        "description": "Cohere is a research organization focused on developing and advancing AI technology.",
        "url": "https://cohere.com",
        "models": ["command-2", "command-2-pro", "command-2-pro-20240620"],
    },
    {
        "name": "HuggingFace",
        "description": "HuggingFace is a research organization focused on developing and advancing AI technology.",
        "url": "https://huggingface.co",
        "models": ["gpt-2", "gpt-2-medium", "gpt-2-large", "gpt-2-xl"],
    },
]
