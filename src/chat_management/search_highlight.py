```python
import re
from src.chat_management.message_schema import MessageSchema

class SearchHighlight:
    def __init__(self):
        self.message_schema = MessageSchema()

    def search_messages(self, chat_id, search_term):
        chat_messages = self.message_schema.get_messages(chat_id)
        search_results = []

        for message in chat_messages:
            if re.search(search_term, message['content'], re.IGNORECASE):
                search_results.append(message)

        return search_results

    def highlight_search_term(self, search_results, search_term):
        highlighted_results = []

        for message in search_results:
            highlighted_message = re.sub(search_term, f'<mark>{search_term}</mark>', message['content'], flags=re.IGNORECASE)
            message['content'] = highlighted_message
            highlighted_results.append(message)

        return highlighted_results
```