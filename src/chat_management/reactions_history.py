```python
from typing import List, Dict
from src.data_schemas import MessageSchema

def get_reactions_history(chat_id: str, message_id: str) -> List[Dict]:
    """
    Function to get the reactions history of a specific message in a chat.
    """
    # Fetch the message from the database
    message = MessageSchema.objects.get(chat_id=chat_id, message_id=message_id)

    # Return the reactions history
    return message.reactions_history

def add_reaction(chat_id: str, message_id: str, user_id: str, reaction: str):
    """
    Function to add a reaction to a specific message in a chat.
    """
    # Fetch the message from the database
    message = MessageSchema.objects.get(chat_id=chat_id, message_id=message_id)

    # Add the reaction to the reactions history
    message.reactions_history.append({
        "user_id": user_id,
        "reaction": reaction,
        "timestamp": datetime.datetime.now()
    })

    # Save the message
    message.save()

def remove_reaction(chat_id: str, message_id: str, user_id: str, reaction: str):
    """
    Function to remove a reaction from a specific message in a chat.
    """
    # Fetch the message from the database
    message = MessageSchema.objects.get(chat_id=chat_id, message_id=message_id)

    # Remove the reaction from the reactions history
    message.reactions_history = [r for r in message.reactions_history if r["user_id"] != user_id or r["reaction"] != reaction]

    # Save the message
    message.save()
```