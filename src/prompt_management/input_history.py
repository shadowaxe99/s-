```python
from collections import deque

class InputHistory:
    def __init__(self, user_id, max_length=100):
        self.user_id = user_id
        self.max_length = max_length
        self._history = deque(maxlen=max_length)

    def add_input(self, input):
        self._history.appendleft(input)

    def get_history(self):
        return list(self._history)

    def clear_history(self):
        self._history.clear()

    def get_last_input(self):
        return self._history[0] if self._history else None
```