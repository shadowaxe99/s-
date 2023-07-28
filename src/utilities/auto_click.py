```python
import pyautogui

def auto_click(x, y, duration=0.1):
    """
    Function to automate mouse click at a given position.
    :param x: x-coordinate of the position.
    :param y: y-coordinate of the position.
    :param duration: duration of the click.
    """
    pyautogui.click(x, y, duration=duration)

def auto_click_element(element_id, duration=0.1):
    """
    Function to automate mouse click on a given DOM element.
    :param element_id: ID of the DOM element.
    :param duration: duration of the click.
    """
    element = pyautogui.locateOnScreen(f'assets/{element_id}.png')
    if element is not None:
        pyautogui.click(element, duration=duration)
    else:
        print(f"Element with ID {element_id} not found.")
```
