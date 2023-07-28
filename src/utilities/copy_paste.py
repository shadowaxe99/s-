```python
import pyperclip

def copy_text(text):
    """
    Function to copy text to clipboard
    """
    pyperclip.copy(text)

def paste_text():
    """
    Function to paste text from clipboard
    """
    return pyperclip.paste()
```