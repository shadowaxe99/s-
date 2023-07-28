```python
from openai import GPT3ChatCompletion

class PersonalityCustomization:
    def __init__(self, user_id, chat_id):
        self.user_id = user_id
        self.chat_id = chat_id

    def get_user_chat(self):
        # Fetch user and chat data from database
        # This is a placeholder and should be replaced with actual database fetching code
        user_data = {"name": "John Doe", "personality": "friendly"}
        chat_data = {"id": self.chat_id, "messages": []}
        return user_data, chat_data

    def customize_chat(self, personality):
        user_data, chat_data = self.get_user_chat()
        user_data["personality"] = personality
        # Update user data in database
        # This is a placeholder and should be replaced with actual database update code
        print(f"Updated user {self.user_id}'s personality to {personality}")

    def generate_message(self, message):
        user_data, chat_data = self.get_user_chat()
        chat_data["messages"].append(message)
        # Generate a response using ChatGPT with the user's personality
        response = GPT3ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a {user_data['personality']} assistant."},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message['content']

    def send_message(self, message):
        response = self.generate_message(message)
        # Send the response to the chat
        # This is a placeholder and should be replaced with actual message sending code
        print(f"Sent message to chat {self.chat_id}: {response}")
```