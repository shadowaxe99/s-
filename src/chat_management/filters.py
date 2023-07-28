```python
from typing import List
from src.chat_management.message_schema import MessageSchema

class ChatFilters:
    def __init__(self, messages: List[MessageSchema]):
        self.messages = messages

    def filter_by_user(self, user_id: str) -> List[MessageSchema]:
        return [message for message in self.messages if message.user_id == user_id]

    def filter_by_content(self, keyword: str) -> List[MessageSchema]:
        return [message for message in self.messages if keyword in message.content]

    def filter_by_sentiment(self, sentiment: str) -> List[MessageSchema]:
        return [message for message in self.messages if message.sentiment == sentiment]

    def filter_by_emotion(self, emotion: str) -> List[MessageSchema]:
        return [message for message in self.messages if message.emotion == emotion]

    def filter_by_language(self, language_id: str) -> List[MessageSchema]:
        return [message for message in self.messages if message.language_id == language_id]
```