```python
from typing import Dict
from src.chat_management.message_schema import MessageSchema

class MessagePinning:
    def __init__(self):
        self.pinned_messages = {}

    def pin_message(self, user_id: str, chat_id: str, message_id: str, message: Dict[str, str]) -> None:
        if user_id not in self.pinned_messages:
            self.pinned_messages[user_id] = {}
        if chat_id not in self.pinned_messages[user_id]:
            self.pinned_messages[user_id][chat_id] = {}
        self.pinned_messages[user_id][chat_id][message_id] = message

    def unpin_message(self, user_id: str, chat_id: str, message_id: str) -> None:
        if user_id in self.pinned_messages and chat_id in self.pinned_messages[user_id]:
            self.pinned_messages[user_id][chat_id].pop(message_id, None)

    def get_pinned_messages(self, user_id: str, chat_id: str) -> Dict[str, MessageSchema]:
        if user_id in self.pinned_messages and chat_id in self.pinned_messages[user_id]:
            return self.pinned_messages[user_id][chat_id]
        return {}
```