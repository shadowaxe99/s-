```python
import pandas as pd
from collections import Counter

class ReactionAnalytics:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.reactions_data = pd.DataFrame()

    def load_reactions(self):
        # Load reactions data from database
        # This is a placeholder, replace with actual database loading code
        self.reactions_data = pd.read_csv(f'database/{self.chat_id}_reactions.csv')

    def count_reactions(self):
        # Count the number of each reaction
        reaction_counts = Counter(self.reactions_data['reaction'])
        return reaction_counts

    def user_reaction_counts(self, user_id):
        # Count the number of each reaction for a specific user
        user_reactions = self.reactions_data[self.reactions_data['user_id'] == user_id]
        user_reaction_counts = Counter(user_reactions['reaction'])
        return user_reaction_counts

    def message_reaction_counts(self, message_id):
        # Count the number of each reaction for a specific message
        message_reactions = self.reactions_data[self.reactions_data['message_id'] == message_id]
        message_reaction_counts = Counter(message_reactions['reaction'])
        return message_reaction_counts
```