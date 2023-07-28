```python
import os
import json
from datetime import datetime

# Importing shared dependencies
from src.shared_dependencies import UserSchema, ChatSchema, MessageSchema

class AutoSync:
    def __init__(self, user_id, chat_id):
        self.user_id = user_id
        self.chat_id = chat_id

    def get_chat_data(self):
        # Load chat data from the database
        chat_data = ChatSchema.load_chat(self.chat_id)
        return chat_data

    def get_user_data(self):
        # Load user data from the database
        user_data = UserSchema.load_user(self.user_id)
        return user_data

    def sync(self):
        # Get chat and user data
        chat_data = self.get_chat_data()
        user_data = self.get_user_data()

        # Prepare data for syncing
        data_to_sync = {
            "user": user_data,
            "chat": chat_data,
            "last_synced": datetime.now().isoformat()
        }

        # Convert data to json
        json_data = json.dumps(data_to_sync)

        # Write data to a file
        with open(f"{self.user_id}_{self.chat_id}_sync.json", "w") as file:
            file.write(json_data)

        print("Auto sync completed.")

# Usage
auto_sync = AutoSync("user123", "chat456")
auto_sync.sync()
```