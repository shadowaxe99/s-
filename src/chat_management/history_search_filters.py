```python
from typing import List
from src.chat_management.message_schema import MessageSchema

class HistorySearchFilters:
    def __init__(self, messages: List[MessageSchema]):
        self.messages = messages

    def filter_by_user(self, user_id: str):
        return [message for message in self.messages if message.user_id == user_id]

    def filter_by_date(self, start_date: str, end_date: str):
        return [message for message in self.messages if start_date <= message.timestamp <= end_date]

    def filter_by_keyword(self, keyword: str):
        return [message for message in self.messages if keyword in message.content]

    def filter_by_sentiment(self, sentiment: str):
        return [message for message in self.messages if message.sentiment == sentiment]

    def filter_by_emotion(self, emotion: str):
        return [message for message in self.messages if message.emotion == emotion]
```