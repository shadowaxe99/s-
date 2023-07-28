```python
import tkinter as tk

class ShortKeys:
    def __init__(self, root):
        self.root = root
        self.bind_short_keys()

    def bind_short_keys(self):
        self.root.bind('<Command-c>', self.copy)
        self.root.bind('<Command-v>', self.paste)
        self.root.bind('<Command-x>', self.cut)
        self.root.bind('<Command-z>', self.undo)
        self.root.bind('<Command-y>', self.redo)
        self.root.bind('<Command-s>', self.save)
        self.root.bind('<Command-o>', self.open)
        self.root.bind('<Command-n>', self.new)
        self.root.bind('<Command-f>', self.find)
        self.root.bind('<Command-a>', self.select_all)

    def copy(self, event=None):
        self.root.event_generate('<<Copy>>')
        return 'break'

    def paste(self, event=None):
        self.root.event_generate('<<Paste>>')
        return 'break'

    def cut(self, event=None):
        self.root.event_generate('<<Cut>>')
        return 'break'

    def undo(self, event=None):
        self.root.event_generate('<<Undo>>')
        return 'break'

    def redo(self, event=None):
        self.root.event_generate('<<Redo>>')
        return 'break'

    def save(self, event=None):
        # Implement save functionality here
        pass

    def open(self, event=None):
        # Implement open functionality here
        pass

    def new(self, event=None):
        # Implement new functionality here
        pass

    def find(self, event=None):
        # Implement find functionality here
        pass

    def select_all(self, event=None):
        self.root.event_generate('<<SelectAll>>')
        return 'break'

root = tk.Tk()
app = ShortKeys(root)
root.mainloop()
```