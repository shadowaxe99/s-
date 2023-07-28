```python
import tkinter as tk

class ScrollUtility:
    def __init__(self, root):
        self.root = root

    def scroll_to_top(self, element_id):
        widget = self.root.nametowidget(element_id)
        if isinstance(widget, (tk.Text, tk.Listbox, tk.Canvas)):
            widget.yview_moveto(0)
        elif isinstance(widget, tk.Scrollbar):
            widget.set(0, 0.1)

    def scroll_to_bottom(self, element_id):
        widget = self.root.nametowidget(element_id)
        if isinstance(widget, (tk.Text, tk.Listbox, tk.Canvas)):
            widget.yview_moveto(1)
        elif isinstance(widget, tk.Scrollbar):
            widget.set(0.9, 1)
```