```python
from typing import List, Dict
from src.shared_dependencies import PromptSchema, prompt_id

class PromptTemplate:
    def __init__(self):
        self.templates = {}

    def add_template(self, id: str, template: PromptSchema) -> None:
        self.templates[id] = template

    def remove_template(self, id: str) -> None:
        if id in self.templates:
            del self.templates[id]

    def get_template(self, id: str) -> PromptSchema:
        return self.templates.get(id, None)

    def get_all_templates(self) -> Dict[str, PromptSchema]:
        return self.templates

prompt_template = PromptTemplate()

def create_prompt_template(id: str, prompt: str, user_id: str) -> None:
    new_template = PromptSchema(prompt_id=id, prompt=prompt, user_id=user_id)
    prompt_template.add_template(id, new_template)

def delete_prompt_template(id: str) -> None:
    prompt_template.remove_template(id)

def get_prompt_template(id: str) -> PromptSchema:
    return prompt_template.get_template(id)

def get_all_prompt_templates() -> Dict[str, PromptSchema]:
    return prompt_template.get_all_templates()
```