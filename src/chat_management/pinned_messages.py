```python
from src.chat_management.message_schema import MessageSchema

class PinnedMessages:
    def __init__(self):
        self.pinned_messages = []

    def pin_message(self, message_id, user_id):
        message = MessageSchema.get_message(message_id, user_id)
        if message:
            self.pinned_messages.append(message)
            return True
        return False

    def unpin_message(self, message_id, user_id):
        for message in self.pinned_messages:
            if message['message_id'] == message_id and message['user_id'] == user_id:
                self.pinned_messages.remove(message)
                return True
        return False

    def get_pinned_messages(self, user_id):
        return [message for message in self.pinned_messages if message['user_id'] == user_id]
```