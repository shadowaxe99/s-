```python
from cryptography.fernet import Fernet

class ChatEncryption:

    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_message(self, message):
        cipher_text = self.cipher_suite.encrypt(message.encode())
        return cipher_text

    def decrypt_message(self, cipher_text):
        plain_text = self.cipher_suite.decrypt(cipher_text)
        return plain_text.decode()

# Usage
# chat_encryption = ChatEncryption()
# encrypted_message = chat_encryption.encrypt_message("Hello World")
# decrypted_message = chat_encryption.decrypt_message(encrypted_message)
```