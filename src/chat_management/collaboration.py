```python
from typing import List
from dataclasses import dataclass

@dataclass
class User:
    user_id: str

@dataclass
class Message:
    message_id: str
    user: User
    content: str

@dataclass
class Chat:
    chat_id: str
    users: List[User]
    messages: List[Message]

def add_user_to_chat(chat: Chat, user: User) -> None:
    if user not in chat.users:
        chat.users.append(user)

def remove_user_from_chat(chat: Chat, user: User) -> None:
    if user in chat.users:
        chat.users.remove(user)

def send_message_in_chat(chat: Chat, user: User, message_content: str) -> None:
    if user in chat.users:
        message = Message(message_id=str(len(chat.messages)), user=user, content=message_content)
        chat.messages.append(message)
    else:
        raise Exception("User not in chat")

def get_chat_messages(chat: Chat) -> List[Message]:
    return chat.messages
```