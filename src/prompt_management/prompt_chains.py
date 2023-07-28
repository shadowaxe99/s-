```python
from typing import List
from src.utilities.model_switcher import switch_model
from src.utilities.word_character_count import count_words_characters

class PromptChain:
    def __init__(self, user_id: str, prompt_id: str):
        self.user_id = user_id
        self.prompt_id = prompt_id
        self.chain = []

    def add_to_chain(self, message_id: str):
        self.chain.append(message_id)

    def remove_from_chain(self, message_id: str):
        self.chain.remove(message_id)

    def get_chain(self) -> List[str]:
        return self.chain

    def clear_chain(self):
        self.chain = []

    def switch_model_in_chain(self, model_name: str):
        for message_id in self.chain:
            switch_model(self.user_id, message_id, model_name)

    def count_words_characters_in_chain(self) -> dict:
        total_words = 0
        total_characters = 0
        for message_id in self.chain:
            count = count_words_characters(self.user_id, message_id)
            total_words += count['words']
            total_characters += count['characters']
        return {'words': total_words, 'characters': total_characters}
```