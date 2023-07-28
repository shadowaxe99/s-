```python
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

class VoiceRecording:
    def __init__(self, user_id, chat_id):
        self.user_id = user_id
        self.chat_id = chat_id
        self.fs = 44100  # Sample rate
        self.seconds = 3  # Duration of recording

    def record_voice(self):
        myrecording = sd.rec(int(self.seconds * self.fs), samplerate=self.fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write('output.wav', self.fs, myrecording)  # Save as WAV file 

    def send_voice_message(self):
        self.record_voice()
        # Here you would typically use the 'output.wav' file and send it as a message
        # This depends on your specific chat implementation
        # For example, you might use a function like this:
        # self.chat.send_voice_message(self.user_id, self.chat_id, 'output.wav')
```