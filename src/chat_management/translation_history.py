```python
from typing import List, Dict
from src.chat_management.message_schema import MessageSchema

class TranslationHistory:
    def __init__(self):
        self.translation_history = {}

    def add_translation(self, message_id: str, original_text: str, translated_text: str, language_id: str):
        if message_id not in self.translation_history:
            self.translation_history[message_id] = []
        self.translation_history[message_id].append({
            'original_text': original_text,
            'translated_text': translated_text,
            'language_id': language_id
        })

    def get_translation_history(self, message_id: str) -> List[Dict[str, str]]:
        return self.translation_history.get(message_id, [])

    def clear_translation_history(self, message_id: str):
        if message_id in self.translation_history:
            del self.translation_history[message_id]

    def clear_all_translation_history(self):
        self.translation_history = {}
```