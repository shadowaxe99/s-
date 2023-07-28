```python
class CopyMode:
    def __init__(self):
        self.is_copy_mode = False

    def toggle_copy_mode(self):
        self.is_copy_mode = not self.is_copy_mode

    def copy_message(self, message_id):
        if not self.is_copy_mode:
            print("Copy mode is not enabled.")
            return

        # Assuming MessageSchema has a method to get message by id
        message = MessageSchema.get_message_by_id(message_id)
        if not message:
            print(f"No message found with id: {message_id}")
            return

        # Copy message to clipboard
        self.copy_to_clipboard(message)

    @staticmethod
    def copy_to_clipboard(text):
        command = 'echo ' + text.strip() + '| pbcopy'
        os.system(command)

copy_mode = CopyMode()
```
