from cryptography.fernet import Fernet
from config import Config
import random

class MessageHandler:
    def __init__(self):
        self.cipher = Fernet(Config.ENCRYPTION_KEY.encode())
        self.previous_messages = set()

    def generate_message(self):
        messages = [
            "Hacker with evil look 😈",
            "Security is paramount 🔒",
            "Stay vigilant, stay safe! ☠️",
        ]
        # Avoid repeating messages
        new_message = random.choice(messages)
        while new_message in self.previous_messages:
            new_message = random.choice(messages)
        self.previous_messages.add(new_message)
        return f"{new_message}\nAdmin - {Config.ADMIN_CONTACT}"

    def encrypt_message(self, message):
        return self.cipher.encrypt(message.encode()).decode()

    def send_message(self, group_id, api_client):
        if group_id not in Config.ALLOWED_GROUPS:
            print(f"Group {group_id} is not permitted to receive messages.")
            return
        message = self.generate_message()
        encrypted_message = self.encrypt_message(message)
        api_client.send_group_message(group_id, encrypted_message)
        print(f"Message sent to group {group_id}: {encrypted_message}")