from ai_provider.ai_provider_abc import AIProvider
from openai import OpenAI

class OpenAIProvider(AIProvider):
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        
    def generate_text(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-3.5-turbo",
        )
        return response['choices'][0]['message']['content']
