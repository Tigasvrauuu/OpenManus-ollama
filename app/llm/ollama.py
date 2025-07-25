from openai import AsyncOpenAI


class OllamaClient:
    def __init__(self, api_key: str, base_url: str):
        self.client = AsyncOpenAI(api_key=api_key, base_url=base_url)

    @property
    def chat(self):
        return self.client.chat
