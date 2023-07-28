```python
from schemas import MessageSchema, UserSchema

class ModerationTools:
    def __init__(self):
        self.banned_users = set()
        self.muted_users = set()

    def ban_user(self, user_id: str, user_schema: UserSchema):
        if user_schema.validate_user(user_id):
            self.banned_users.add(user_id)
            return f"User {user_id} has been banned."
        else:
            return "Invalid user ID."

    def unban_user(self, user_id: str, user_schema: UserSchema):
        if user_schema.validate_user(user_id):
            self.banned_users.remove(user_id)
            return f"User {user_id} has been unbanned."
        else:
            return "Invalid user ID."

    def mute_user(self, user_id: str, user_schema: UserSchema):
        if user_schema.validate_user(user_id):
            self.muted_users.add(user_id)
            return f"User {user_id} has been muted."
        else:
            return "Invalid user ID."

    def unmute_user(self, user_id: str, user_schema: UserSchema):
        if user_schema.validate_user(user_id):
            self.muted_users.remove(user_id)
            return f"User {user_id} has been unmuted."
        else:
            return "Invalid user ID."

    def delete_message(self, message_id: str, message_schema: MessageSchema):
        if message_schema.validate_message(message_id):
            # Assuming delete_message() is a function in message_schema that deletes a message
            message_schema.delete_message(message_id)
            return f"Message {message_id} has been deleted."
        else:
            return "Invalid message ID."
```