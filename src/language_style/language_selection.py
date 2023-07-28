```python
from typing import Dict

class LanguageSelection:
    def __init__(self):
        self.languages = {
            "en": "English",
            "es": "Spanish",
            "fr": "French",
            "de": "German",
            "it": "Italian",
            "pt": "Portuguese",
            "ru": "Russian",
            "ja": "Japanese",
            "zh": "Chinese",
            "ko": "Korean",
            "ar": "Arabic"
        }
        self.selected_language = "en"

    def get_languages(self) -> Dict[str, str]:
        return self.languages

    def get_selected_language(self) -> str:
        return self.selected_language

    def set_selected_language(self, language_id: str):
        if language_id in self.languages:
            self.selected_language = language_id
        else:
            raise ValueError(f"Invalid language id: {language_id}")

    def translate_text(self, text: str, target_language: str) -> str:
        # This function should be implemented with a real translation service
        # Here we just return the original text for simplicity
        return text
```