```python
import datetime
from src.chat_management.message_schema import MessageSchema

class Reminder:
    def __init__(self, message_id, time):
        self.message_id = message_id
        self.time = time

class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, message_id, time):
        reminder = Reminder(message_id, time)
        self.reminders.append(reminder)

    def remove_reminder(self, message_id):
        self.reminders = [reminder for reminder in self.reminders if reminder.message_id != message_id]

    def get_reminders(self, user_id):
        user_reminders = []
        for reminder in self.reminders:
            message = MessageSchema.get_message(reminder.message_id)
            if message and message['user_id'] == user_id:
                user_reminders.append(reminder)
        return user_reminders

    def check_reminders(self):
        current_time = datetime.datetime.now()
        for reminder in self.reminders:
            if reminder.time <= current_time:
                message = MessageSchema.get_message(reminder.message_id)
                if message:
                    print(f"Reminder for message {message['content']} at {reminder.time}")
                    self.remove_reminder(reminder.message_id)
```