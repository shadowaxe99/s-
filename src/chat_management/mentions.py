```python
from typing import List
from src.chat_management.message import Message

class Mention:
    def __init__(self, user_id: str, message_id: str):
        self.user_id = user_id
        self.message_id = message_id

class MentionsManager:
    def __init__(self):
        self.mentions = []

    def add_mention(self, user_id: str, message_id: str):
        mention = Mention(user_id, message_id)
        self.mentions.append(mention)

    def remove_mention(self, user_id: str, message_id: str):
        self.mentions = [mention for mention in self.mentions if not (mention.user_id == user_id and mention.message_id == message_id)]

    def get_mentions_for_user(self, user_id: str) -> List[Message]:
        return [mention for mention in self.mentions if mention.user_id == user_id]

    def clear_mentions_for_user(self, user_id: str):
        self.mentions = [mention for mention in self.mentions if mention.user_id != user_id]
```