```python
import os
from typing import List
from prompt_management.prompt_schemas import PromptSchema

class QuickAccess:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.quick_access_file = f"{self.user_id}_quick_access.txt"

    def add_to_quick_access(self, prompt_id: str):
        with open(self.quick_access_file, 'a') as file:
            file.write(f"{prompt_id}\n")

    def remove_from_quick_access(self, prompt_id: str):
        prompts = self.get_quick_access_prompts()
        prompts.remove(prompt_id)
        with open(self.quick_access_file, 'w') as file:
            for prompt in prompts:
                file.write(f"{prompt}\n")

    def get_quick_access_prompts(self) -> List[str]:
        if not os.path.exists(self.quick_access_file):
            return []
        with open(self.quick_access_file, 'r') as file:
            prompts = file.readlines()
        return [prompt.strip() for prompt in prompts]

    def is_in_quick_access(self, prompt_id: str) -> bool:
        return prompt_id in self.get_quick_access_prompts()
```