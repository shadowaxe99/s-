```python
import openai

class ModelSwitcher:
    def __init__(self):
        self.current_model = 'gpt-3.5-turbo'

    def switch_model(self, model_name):
        if model_name in openai.api.models:
            self.current_model = model_name
            print(f"Model switched to {model_name}")
        else:
            print(f"Model {model_name} is not available.")

    def get_current_model(self):
        return self.current_model
```