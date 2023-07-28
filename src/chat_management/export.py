```python
import json
from typing import Dict
from src.chat_management.message_schema import MessageSchema

def export_chat(chat_id: str, user_id: str) -> None:
    """
    Function to export a chat as a JSON file.
    """
    # Fetch chat data
    chat_data = fetch_chat_data(chat_id, user_id)

    # Convert chat data to JSON
    chat_json = json.dumps(chat_data, indent=4, cls=MessageSchema)

    # Write JSON data to file
    with open(f'{chat_id}_export.json', 'w') as file:
        file.write(chat_json)

def fetch_chat_data(chat_id: str, user_id: str) -> Dict:
    """
    Function to fetch chat data. This is a placeholder and should be replaced with actual implementation.
    """
    # Placeholder chat data
    chat_data = {
        "chat_id": chat_id,
        "user_id": user_id,
        "messages": [
            {
                "message_id": "1",
                "content": "Hello, world!",
                "timestamp": "2022-01-01T00:00:00Z"
            },
            {
                "message_id": "2",
                "content": "Goodbye, world!",
                "timestamp": "2022-01-01T00:01:00Z"
            }
        ]
    }

    return chat_data
```