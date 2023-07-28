```python
import os
from plyer import notification

class ChatNotification:
    def __init__(self, user_id, chat_id, message_id):
        self.user_id = user_id
        self.chat_id = chat_id
        self.message_id = message_id

    def notify(self, title, message):
        notification.notify(
            title=title,
            message=message,
            app_icon=None,
            timeout=10,
        )

    def new_message_notification(self, message):
        title = f"New Message in Chat {self.chat_id}"
        self.notify(title, message)

    def deleted_message_notification(self):
        title = f"Message Deleted in Chat {self.chat_id}"
        message = f"Message {self.message_id} has been deleted."
        self.notify(title, message)

    def edited_message_notification(self):
        title = f"Message Edited in Chat {self.chat_id}"
        message = f"Message {self.message_id} has been edited."
        self.notify(title, message)
```