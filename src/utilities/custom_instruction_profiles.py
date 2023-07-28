```python
import json

class CustomInstructionProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.profiles = self.load_profiles()

    def load_profiles(self):
        try:
            with open(f'{self.user_id}_instruction_profiles.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_profiles(self):
        with open(f'{self.user_id}_instruction_profiles.json', 'w') as file:
            json.dump(self.profiles, file)

    def create_profile(self, profile_name, instructions):
        self.profiles[profile_name] = instructions
        self.save_profiles()

    def delete_profile(self, profile_name):
        if profile_name in self.profiles:
            del self.profiles[profile_name]
            self.save_profiles()

    def edit_profile(self, profile_name, instructions):
        if profile_name in self.profiles:
            self.profiles[profile_name] = instructions
            self.save_profiles()

    def get_profile(self, profile_name):
        return self.profiles.get(profile_name, None)
```