```python
from typing import Dict
from src.chat_management.message_schema import MessageSchema

class ChatTemplates:
    def __init__(self):
        self.templates = {}

    def create_template(self, template_id: str, template: Dict[str, str]) -> None:
        """
        Create a new chat template.
        """
        self.templates[template_id] = template

    def get_template(self, template_id: str) -> Dict[str, str]:
        """
        Get a chat template by its ID.
        """
        return self.templates.get(template_id, None)

    def delete_template(self, template_id: str) -> None:
        """
        Delete a chat template by its ID.
        """
        if template_id in self.templates:
            del self.templates[template_id]

    def apply_template(self, template_id: str, message: MessageSchema) -> MessageSchema:
        """
        Apply a chat template to a message.
        """
        template = self.get_template(template_id)
        if template is None:
            return message

        for key, value in template.items():
            if hasattr(message, key):
                setattr(message, key, value)

        return message
```