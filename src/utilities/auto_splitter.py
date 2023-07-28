```python
class AutoSplitter:
    def __init__(self, max_length):
        self.max_length = max_length

    def split_message(self, message):
        words = message.split(' ')
        messages = []
        current_message = ''
        
        for word in words:
            if len(current_message + ' ' + word) <= self.max_length:
                current_message += ' ' + word
            else:
                messages.append(current_message)
                current_message = word

        if current_message:
            messages.append(current_message)

        return messages
```