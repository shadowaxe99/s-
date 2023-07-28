```python
from schemas import MessageSchema

def editMessage(message_id, new_content):
    """
    Function to edit a message in a chat.
    Args:
    message_id : str : Unique identifier for the message to be edited.
    new_content : str : New content for the message.
    Returns:
    bool : True if the operation was successful, False otherwise.
    """
    # Fetch the message from the database
    message = MessageSchema.objects.get(id=message_id)

    # Check if the message exists
    if not message:
        print(f"Message with id {message_id} does not exist.")
        return False

    # Edit the message content
    message.content = new_content

    # Save the changes to the database
    message.save()

    print(f"Message with id {message_id} has been edited.")
    return True
```