```python
from typing import Dict, List
from src.chat_management.message_schema import MessageSchema

class ThreadedReplies:
    def __init__(self):
        self.threads = {}  # Dictionary to store threads. Key: message_id, Value: List of reply message_ids

    def add_reply(self, message_id: str, reply_message: MessageSchema):
        if message_id in self.threads:
            self.threads[message_id].append(reply_message.message_id)
        else:
            self.threads[message_id] = [reply_message.message_id]

    def get_replies(self, message_id: str) -> List[str]:
        return self.threads.get(message_id, [])

    def delete_reply(self, message_id: str, reply_message_id: str):
        if message_id in self.threads:
            try:
                self.threads[message_id].remove(reply_message_id)
            except ValueError:
                pass

    def delete_thread(self, message_id: str):
        if message_id in self.threads:
            del self.threads[message_id]
```