```python
import speech_recognition as sr

class ChatTranscription:
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.transcript = ""

    def transcribe_audio(self):
        r = sr.Recognizer()
        with sr.AudioFile(self.audio_file) as source:
            audio_data = r.record(source)
            self.transcript = r.recognize_google(audio_data)
        return self.transcript

    def get_transcript(self):
        if not self.transcript:
            self.transcribe_audio()
        return self.transcript
```