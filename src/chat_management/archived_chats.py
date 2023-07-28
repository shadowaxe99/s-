```python
from typing import List
from src.chat_management.message_schema import MessageSchema

class ArchivedChats:
    def __init__(self):
        self.archived_chats = {}

    def archive_chat(self, chat_id: str, messages: List[MessageSchema]):
        if chat_id not in self.archived_chats:
            self.archived_chats[chat_id] = messages

    def unarchive_chat(self, chat_id: str):
        if chat_id in self.archived_chats:
            return self.archived_chats.pop(chat_id)
        else:
            return None

    def get_archived_chat(self, chat_id: str):
        return self.archived_chats.get(chat_id, None)

    def get_all_archived_chats(self):
        return self.archived_chats
```