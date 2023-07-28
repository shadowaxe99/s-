```python
from typing import List
from dataclasses import dataclass

@dataclass
class Emoji:
    id: str
    name: str
    unicode: str

@dataclass
class Reaction:
    user_id: str
    emoji: Emoji

class EmojisReactions:
    def __init__(self):
        self.reactions = {}

    def add_reaction(self, message_id: str, reaction: Reaction):
        if message_id not in self.reactions:
            self.reactions[message_id] = []
        self.reactions[message_id].append(reaction)

    def remove_reaction(self, message_id: str, user_id: str, emoji_id: str):
        if message_id in self.reactions:
            self.reactions[message_id] = [reaction for reaction in self.reactions[message_id] if not (reaction.user_id == user_id and reaction.emoji.id == emoji_id)]

    def get_reactions(self, message_id: str) -> List[Reaction]:
        return self.reactions.get(message_id, [])

    def get_reaction_count(self, message_id: str, emoji_id: str) -> int:
        if message_id in self.reactions:
            return len([reaction for reaction in self.reactions[message_id] if reaction.emoji.id == emoji_id])
        return 0
```