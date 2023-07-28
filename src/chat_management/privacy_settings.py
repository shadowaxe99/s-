```python
from schemas import UserSchema, ChatSchema

class PrivacySettings:
    def __init__(self, user_id, chat_id):
        self.user_id = user_id
        self.chat_id = chat_id

    def get_user_privacy_settings(self):
        user_data = UserSchema.objects.get(id=self.user_id)
        return user_data.privacy_settings

    def update_user_privacy_settings(self, new_settings):
        user_data = UserSchema.objects.get(id=self.user_id)
        user_data.update(privacy_settings=new_settings)

    def get_chat_privacy_settings(self):
        chat_data = ChatSchema.objects.get(id=self.chat_id)
        return chat_data.privacy_settings

    def update_chat_privacy_settings(self, new_settings):
        chat_data = ChatSchema.objects.get(id=self.chat_id)
        chat_data.update(privacy_settings=new_settings)
```