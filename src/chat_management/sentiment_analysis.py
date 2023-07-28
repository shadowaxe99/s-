```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalysis:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, message_id, message_text):
        sentiment_score = self.sia.polarity_scores(message_text)
        return sentiment_score

    def update_message_sentiment(self, message_id, sentiment_score):
        # Assuming we have a MessageSchema that has a sentiment field
        message = MessageSchema.objects.get(id=message_id)
        message.sentiment = sentiment_score
        message.save()

    def process_message(self, message_id, message_text):
        sentiment_score = self.analyze_sentiment(message_id, message_text)
        self.update_message_sentiment(message_id, sentiment_score)

# Usage
# sentiment_analysis = SentimentAnalysis()
# sentiment_analysis.process_message(message_id, message_text)
```