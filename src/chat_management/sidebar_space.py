```python
import tkinter as tk

class SidebarSpace:
    def __init__(self, root):
        self.root = root
        self.sidebar_frame = tk.Frame(self.root, width=200, bg='grey')
        self.sidebar_frame.pack(expand=False, fill='both', side='left')

    def expand_sidebar(self):
        self.sidebar_frame.config(width=400)

    def shrink_sidebar(self):
        self.sidebar_frame.config(width=200)

root = tk.Tk()
sidebar = SidebarSpace(root)
root.mainloop()
```