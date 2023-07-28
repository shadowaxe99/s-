```python
import datetime
from src.chat_management.message_schema import MessageSchema

def add_timestamp(message_id):
    """
    Function to add timestamp to a message.
    """
    message = MessageSchema.objects.get(id=message_id)
    message.timestamp = datetime.datetime.now()
    message.save()

def get_timestamp(message_id):
    """
    Function to get the timestamp of a message.
    """
    message = MessageSchema.objects.get(id=message_id)
    return message.timestamp

def update_timestamp(message_id):
    """
    Function to update the timestamp of a message.
    """
    message = MessageSchema.objects.get(id=message_id)
    message.timestamp = datetime.datetime.now()
    message.save()
```