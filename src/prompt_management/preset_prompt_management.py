```python
from typing import List
from src.shared.schemas import PromptSchema

class PresetPromptManager:
    def __init__(self):
        self.preset_prompts = []

    def load_preset_prompts(self, preset_prompts: List[PromptSchema]):
        self.preset_prompts = preset_prompts

    def get_preset_prompt(self, prompt_id: str) -> PromptSchema:
        for prompt in self.preset_prompts:
            if prompt.prompt_id == prompt_id:
                return prompt
        return None

    def add_preset_prompt(self, prompt: PromptSchema):
        self.preset_prompts.append(prompt)

    def remove_preset_prompt(self, prompt_id: str):
        self.preset_prompts = [prompt for prompt in self.preset_prompts if prompt.prompt_id != prompt_id]

    def update_preset_prompt(self, prompt_id: str, updated_prompt: PromptSchema):
        for i, prompt in enumerate(self.preset_prompts):
            if prompt.prompt_id == prompt_id:
                self.preset_prompts[i] = updated_prompt
                return
        raise ValueError(f"Preset prompt with id {prompt_id} not found.")
```