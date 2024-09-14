import os
import re
from ai_provider.ai_provider_abc import AIProvider
from google.generativeai import GenerativeModel, configure



class GoogleGeminiProvider(AIProvider):
    def __init__(self, api_key):
        configure(api_key=api_key)
        self.model = GenerativeModel("gemini-1.5-flash")

    def generate_text(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        html_content = response.text.strip()
        match = re.search(r'<html.*?>([\s\S]*?)<\/html>', html_content, re.IGNORECASE)
        return match.group(0) if match else html_content.strip()