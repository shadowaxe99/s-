```python
import os
from datetime import datetime
from src.chat_management.auto_sync import AutoSync

class QuickSync:
    def __init__(self, user_id, chat_id):
        self.user_id = user_id
        self.chat_id = chat_id
        self.auto_sync = AutoSync(user_id, chat_id)

    def sync(self):
        last_sync_time = self.get_last_sync_time()
        current_time = datetime.now()

        if (current_time - last_sync_time).seconds < 30:
            print("Quick Sync in progress...")
            self.auto_sync.sync()
            self.update_last_sync_time(current_time)
            print("Quick Sync completed.")
        else:
            print("Quick Sync not required. Last sync was less than 30 seconds ago.")

    def get_last_sync_time(self):
        if os.path.exists('last_sync_time.txt'):
            with open('last_sync_time.txt', 'r') as file:
                last_sync_time = datetime.strptime(file.read(), '%Y-%m-%d %H:%M:%S.%f')
        else:
            last_sync_time = datetime.now()
        return last_sync_time

    def update_last_sync_time(self, current_time):
        with open('last_sync_time.txt', 'w') as file:
            file.write(str(current_time))
```