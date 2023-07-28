```python
from schemas import MessageSchema
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['chatgpt_db']
messages = db['messages']

def delete_message(message_id):
    """
    Function to delete a message from the database.
    """
    query = {"message_id": message_id}
    message = messages.find_one(query)
    
    if message:
        messages.delete_one(query)
        print(f"Message with id {message_id} deleted successfully.")
    else:
        print(f"No message found with id {message_id}.")

def delete_chat_messages(chat_id):
    """
    Function to delete all messages from a specific chat.
    """
    query = {"chat_id": chat_id}
    messages_to_delete = messages.find(query)
    
    if messages_to_delete:
        messages.delete_many(query)
        print(f"All messages from chat with id {chat_id} deleted successfully.")
    else:
        print(f"No messages found for chat with id {chat_id}.")
```