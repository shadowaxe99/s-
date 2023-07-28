```python
from typing import List
from dataclasses import dataclass

@dataclass
class Chat:
    chat_id: str
    user_id: str
    folder: str

class FolderManager:
    def __init__(self):
        self.chats = []

    def add_chat(self, chat: Chat):
        self.chats.append(chat)

    def remove_chat(self, chat_id: str):
        self.chats = [chat for chat in self.chats if chat.chat_id != chat_id]

    def move_chat_to_folder(self, chat_id: str, folder: str):
        for chat in self.chats:
            if chat.chat_id == chat_id:
                chat.folder = folder

    def get_chats_in_folder(self, folder: str) -> List[Chat]:
        return [chat for chat in self.chats if chat.folder == folder]

    def reorder_chats_in_folder(self, folder: str, chat_order: List[str]):
        folder_chats = self.get_chats_in_folder(folder)
        folder_chats.sort(key=lambda chat: chat_order.index(chat.chat_id))

folder_manager = FolderManager()
```