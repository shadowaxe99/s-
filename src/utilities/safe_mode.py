```python
class SafeMode:
    def __init__(self):
        self.is_safe_mode = False

    def toggle_safe_mode(self):
        self.is_safe_mode = not self.is_safe_mode
        return self.is_safe_mode

    def get_safe_mode_status(self):
        return self.is_safe_mode

safe_mode = SafeMode()
```