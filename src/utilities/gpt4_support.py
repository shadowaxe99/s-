```python
import openai

class GPT4Support:
    def __init__(self, api_key):
        self.api_key = api_key
        self.model = "gpt-4"

    def set_model(self, model_name):
        self.model = model_name

    def generate_response(self, prompt):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()

    def check_model_support(self):
        supported_models = ["gpt-3", "gpt-4"]
        if self.model in supported_models:
            return True
        else:
            return False
```
