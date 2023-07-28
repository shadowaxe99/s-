```python
from gensim.summarize import summarize

def auto_summarize(text):
    """
    Function to automatically summarize a given text using the Gensim library.
    """
    try:
        summary = summarize(text)
        return summary
    except ValueError:
        return "Text is too short to summarize."

def summarize_chat(chat_id):
    """
    Function to automatically summarize a chat based on its ID.
    """
    # Import the chat data schema and fetch the chat data
    from src.chat_management.ChatSchema import ChatSchema
    chat_data = ChatSchema.get_chat(chat_id)

    # Extract the messages from the chat data
    messages = [message['content'] for message in chat_data['messages']]

    # Join the messages into a single text
    text = ' '.join(messages)

    # Auto-summarize the text
    summary = auto_summarize(text)

    return summary
```