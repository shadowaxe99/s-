```python
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Importing shared dependencies
from schemas import MessageSchema

def analyze_content(message_id):
    # Fetching the message using the shared MessageSchema
    message = MessageSchema.get_message(message_id)
    
    # Tokenizing the message content
    tokens = nltk.word_tokenize(message.content)
    
    # Removing punctuation
    tokens = [token for token in tokens if token.isalpha()]
    
    # Lowercasing
    tokens = [token.lower() for token in tokens]
    
    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Counting word frequencies
    word_frequencies = Counter(tokens)
    
    return word_frequencies
```