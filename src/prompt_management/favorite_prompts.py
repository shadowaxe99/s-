```python
from typing import List
from dataclasses import dataclass

@dataclass
class Prompt:
    id: str
    content: str

class FavoritePrompts:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.favorite_prompts = []

    def add_favorite_prompt(self, prompt: Prompt):
        self.favorite_prompts.append(prompt)

    def remove_favorite_prompt(self, prompt_id: str):
        self.favorite_prompts = [prompt for prompt in self.favorite_prompts if prompt.id != prompt_id]

    def get_favorite_prompts(self) -> List[Prompt]:
        return self.favorite_prompts

    def is_favorite_prompt(self, prompt_id: str) -> bool:
        return any(prompt.id == prompt_id for prompt in self.favorite_prompts)
```