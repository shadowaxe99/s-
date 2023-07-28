```python
from typing import Dict
from src.utilities.word_character_count import count_words_characters

def format_message(message_id: str, formatting_options: Dict[str, str]) -> None:
    """
    Function to format a chat message.
    """
    # Fetch the message from the database using the message_id
    # This is a placeholder function, replace it with actual implementation
    message = fetch_message_from_db(message_id)

    # Apply formatting options
    for option, value in formatting_options.items():
        if option == 'bold':
            message.text = f"<b>{message.text}</b>"
        elif option == 'italic':
            message.text = f"<i>{message.text}</i>"
        elif option == 'underline':
            message.text = f"<u>{message.text}</u>"
        elif option == 'strikethrough':
            message.text = f"<s>{message.text}</s>"
        elif option == 'code':
            message.text = f"<code>{message.text}</code>"
        elif option == 'quote':
            message.text = f"<blockquote>{message.text}</blockquote>"
        elif option == 'link':
            message.text = f"<a href='{value}'>{message.text}</a>"
        elif option == 'color':
            message.text = f"<font color='{value}'>{message.text}</font>"

    # Update the message in the database
    update_message_in_db(message_id, message)

def fetch_message_from_db(message_id: str):
    """
    Placeholder function to fetch a message from the database.
    Replace this with actual implementation.
    """
    pass

def update_message_in_db(message_id: str, message):
    """
    Placeholder function to update a message in the database.
    Replace this with actual implementation.
    """
    pass
```