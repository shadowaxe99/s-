```python
from src.chat_management.ChatSchema import ChatSchema
from src.chat_management.MessageSchema import MessageSchema

def delete_group(chat_id):
    """
    Function to delete a group chat and all its associated messages.
    """
    # Fetch the chat from the database
    chat = ChatSchema.objects.get(chat_id=chat_id)

    # Check if the chat is a group chat
    if chat.is_group:
        # Fetch all messages associated with the chat
        messages = MessageSchema.objects.filter(chat_id=chat_id)

        # Delete all messages
        for message in messages:
            message.delete()

        # Delete the chat
        chat.delete()

        return {"status": "success", "message": "Group chat and all associated messages deleted successfully."}
    else:
        return {"status": "error", "message": "Chat is not a group chat."}
```