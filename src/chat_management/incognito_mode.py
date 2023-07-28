```python
class IncognitoMode:
    def __init__(self):
        self.is_incognito = False

    def toggle_incognito_mode(self):
        self.is_incognito = not self.is_incognito
        return self.is_incognito

    def is_incognito_mode(self):
        return self.is_incognito
```