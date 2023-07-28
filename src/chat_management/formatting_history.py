```python
from typing import List, Dict
from src.chat_management.message_schema import MessageSchema

class FormattingHistory:
    def __init__(self):
        self.formatting_history = {}

    def add_formatting(self, message_id: str, formatting: Dict):
        if message_id in self.formatting_history:
            self.formatting_history[message_id].append(formatting)
        else:
            self.formatting_history[message_id] = [formatting]

    def get_formatting_history(self, message_id: str) -> List[Dict]:
        return self.formatting_history.get(message_id, [])

    def clear_formatting_history(self, message_id: str):
        if message_id in self.formatting_history:
            del self.formatting_history[message_id]

    def clear_all_formatting_history(self):
        self.formatting_history.clear()

if __name__ == "__main__":
    formatting_history = FormattingHistory()
    formatting_history.add_formatting("message1", {"bold": True, "italic": False})
    formatting_history.add_formatting("message1", {"bold": False, "italic": True})
    print(formatting_history.get_formatting_history("message1"))
    formatting_history.clear_formatting_history("message1")
    print(formatting_history.get_formatting_history("message1"))
```