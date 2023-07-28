```python
def count_words_characters(message_id, MessageSchema):
    """
    Function to count the number of words and characters in a message.
    """
    # Fetch the message using the message_id and MessageSchema
    message = MessageSchema.objects.get(id=message_id)

    # Get the text of the message
    text = message.text

    # Count the number of words
    word_count = len(text.split())

    # Count the number of characters
    character_count = len(text)

    return word_count, character_count
```