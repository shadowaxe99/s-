```python
from typing import List
from src.shared_dependencies import PromptSchema, user_id

class CommunityPrompts:
    def __init__(self):
        self.community_prompts = []

    def add_prompt(self, prompt: PromptSchema):
        self.community_prompts.append(prompt)

    def remove_prompt(self, prompt_id: str):
        self.community_prompts = [prompt for prompt in self.community_prompts if prompt.prompt_id != prompt_id]

    def get_prompts(self) -> List[PromptSchema]:
        return self.community_prompts

    def get_prompt_by_user(self, user_id: str) -> List[PromptSchema]:
        return [prompt for prompt in self.community_prompts if prompt.user_id == user_id]

community_prompts = CommunityPrompts()

def add_community_prompt(prompt: PromptSchema):
    community_prompts.add_prompt(prompt)

def remove_community_prompt(prompt_id: str):
    community_prompts.remove_prompt(prompt_id)

def get_community_prompts() -> List[PromptSchema]:
    return community_prompts.get_prompts()

def get_community_prompts_by_user(user_id: str) -> List[PromptSchema]:
    return community_prompts.get_prompt_by_user(user_id)
```