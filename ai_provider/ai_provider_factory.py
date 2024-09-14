import os
from abc import ABC, abstractmethod
from ai_provider.openai import OpenAIProvider
from ai_provider.google_gemini_ai import GoogleGeminiProvider

AI_PROVIDERS = {
    "openai": OpenAIProvider,
    "google_gemini": GoogleGeminiProvider,
}

def get_ai_provider():
    provider_name = os.getenv("AI_PROVIDER")    
    provider_class = AI_PROVIDERS.get(provider_name)

    if provider_class is None:
        raise ValueError(f"Invalid AI provider specified: {provider_name}")
    
    api_key_var = f"{provider_name.upper()}_API_KEY"
    api_key = os.getenv(api_key_var)
    
    if not api_key:
        raise ValueError(f"API key for {provider_name} not found.")
        
    return provider_class(api_key)
