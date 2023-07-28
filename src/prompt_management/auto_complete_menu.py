```python
import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

class AutoCompleteMenu:
    def __init__(self, prompt_id, user_id):
        self.prompt_id = prompt_id
        self.user_id = user_id
        self.prompt_history_file = f'prompt_history_{self.user_id}.txt'
        self.load_prompt_history()

    def load_prompt_history(self):
        if os.path.exists(self.prompt_history_file):
            with open(self.prompt_history_file, 'r') as file:
                self.prompt_history = file.read().splitlines()
        else:
            self.prompt_history = []

    def save_prompt_history(self):
        with open(self.prompt_history_file, 'w') as file:
            for prompt in self.prompt_history:
                file.write(f'{prompt}\n')

    def add_to_prompt_history(self, prompt):
        self.prompt_history.append(prompt)
        self.save_prompt_history()

    def auto_complete_prompt(self):
        prompt_completer = WordCompleter(self.prompt_history, ignore_case=True, sentence=True)
        user_prompt = prompt('Enter your prompt: ', completer=prompt_completer)
        self.add_to_prompt_history(user_prompt)
        return user_prompt
```