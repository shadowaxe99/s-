```python
import json
from textblob import TextBlob
from src.utilities.model_switcher import ModelSwitcher
from src.utilities.word_character_count import count_words_characters

class EmotionAnalysis:
    def __init__(self, user_id, chat_id, message_id):
        self.user_id = user_id
        self.chat_id = chat_id
        self.message_id = message_id
        self.model_switcher = ModelSwitcher()

    def load_message(self):
        # Load the message from the database using the provided IDs
        # This is a placeholder and should be replaced with actual database interaction
        with open(f"database/{self.user_id}/{self.chat_id}/{self.message_id}.json", "r") as file:
            message_data = json.load(file)
        return message_data["content"]

    def analyze_emotion(self):
        # Load the message content
        message_content = self.load_message()

        # Switch to the emotion analysis model
        self.model_switcher.switch_model("emotion_analysis")

        # Analyze the emotion of the message
        analysis = TextBlob(message_content)
        emotion = analysis.sentiment.polarity

        # Switch back to the default model
        self.model_switcher.switch_model("default")

        return emotion

    def save_emotion_analysis(self, emotion):
        # Save the emotion analysis result to the database
        # This is a placeholder and should be replaced with actual database interaction
        with open(f"database/{self.user_id}/{self.chat_id}/{self.message_id}_emotion_analysis.json", "w") as file:
            json.dump({"emotion": emotion}, file)

    def perform_emotion_analysis(self):
        # Perform emotion analysis and save the result
        emotion = self.analyze_emotion()
        self.save_emotion_analysis(emotion)

        # Return the emotion analysis result
        return emotion
```