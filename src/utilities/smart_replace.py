```python
import re

def smart_replace(text, old, new):
    """
    Function to replace old substring with new substring in a smart way.
    It considers word boundaries to avoid replacing substrings of other words.
    """
    word_boundaries = r'\b'
    old = word_boundaries + old + word_boundaries
    return re.sub(old, new, text)
```