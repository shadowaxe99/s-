```python
import tkinter as tk

class Sidebar:
    def __init__(self, root):
        self.root = root
        self.sidebar = tk.Frame(self.root, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
        self.sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

    def toggle_sidebar(self):
        if self.sidebar.winfo_viewable():
            self.hide_sidebar()
        else:
            self.show_sidebar()

    def show_sidebar(self):
        self.sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

    def hide_sidebar(self):
        self.sidebar.pack_forget()

root = tk.Tk()
sidebar = Sidebar(root)
toggle_button = tk.Button(root, text="Toggle Sidebar", command=sidebar.toggle_sidebar)
toggle_button.pack()

root.mainloop()
```