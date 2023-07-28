```python
import requests
from schemas import MessageSchema

class ChatTranslation:
    def __init__(self, target_language):
        self.target_language = target_language

    def translate_message(self, message_id):
        message_data = self.get_message_data(message_id)
        translated_text = self.translate_text(message_data['content'])
        self.update_message_translation(message_id, translated_text)

    def get_message_data(self, message_id):
        # This function should interact with your database and return the message data
        # For the purpose of this example, we will return a dummy data
        return MessageSchema(user_id=1, chat_id=1, message_id=message_id, content="Hello World")

    def translate_text(self, text):
        # This function should interact with a translation API and return the translated text
        # For the purpose of this example, we will use a dummy translation API
        response = requests.get(f'https://api.dummytranslation.com/translate?text={text}&target_language={self.target_language}')
        return response.json()['translated_text']

    def update_message_translation(self, message_id, translated_text):
        # This function should interact with your database and update the message translation
        # For the purpose of this example, we will print the translated text
        print(f'Translated text for message {message_id}: {translated_text}')
```