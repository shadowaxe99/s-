```python
import tkinter as tk

class ConversationWidth:
    def __init__(self, root):
        self.root = root
        self.width_scale = tk.Scale(self.root, from_=200, to=800, orient=tk.HORIZONTAL, length=400, command=self.update_width)
        self.width_scale.set(500)
        self.width_scale.pack()

    def update_width(self, value):
        self.root.geometry(f"{int(value)}x600")

def main():
    root = tk.Tk()
    root.geometry("500x600")
    ConversationWidth(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```
This Python script uses the tkinter library to create a GUI application. The ConversationWidth class creates a horizontal scale (slider) that allows the user to adjust the width of the conversation window. The update_width method is called whenever the slider is moved, updating the width of the window accordingly. The main function initializes the tkinter root window and creates an instance of the ConversationWidth class.