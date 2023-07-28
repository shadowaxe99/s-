```python
import pandas as pd
from src.chat_management.message_schema import MessageSchema

class ChatAnalytics:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.message_schema = MessageSchema()

    def get_chat_data(self):
        chat_data = self.message_schema.get_chat_messages(self.chat_id)
        return chat_data

    def generate_report(self):
        chat_data = self.get_chat_data()
        df = pd.DataFrame(chat_data)

        report = {
            'total_messages': len(df),
            'unique_users': df['user_id'].nunique(),
            'most_active_user': df['user_id'].value_counts().idxmax(),
            'average_message_length': df['message_content'].str.len().mean(),
            'most_common_words': df['message_content'].str.split(expand=True).stack().value_counts().head(10).to_dict()
        }

        return report
```
