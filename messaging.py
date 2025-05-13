from cryptography.fernet import Fernet
from config import Config
import random
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class MessageHandler:
    def __init__(self):
        try:
            self.cipher = Fernet(Config.ENCRYPTION_KEY.encode())
        except Exception as e:
            logger.error("Failed to initialize encryption. Check your ENCRYPTION_KEY: %s", e)
            raise
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
        retries = 3
        for attempt in range(retries):
            try:
                return self.cipher.encrypt(message.encode()).decode()
            except Exception as e:
                logger.error("Encryption failed (Attempt %d/%d): %s", attempt + 1, retries, e)
                time.sleep(1)
        raise Exception("Encryption failed after multiple attempts.")

    def send_message(self, group_id, api_client):
        if group_id not in Config.ALLOWED_GROUPS:
            logger.warning("Group %s is not permitted to receive messages.", group_id)
            return
        try:
            message = self.generate_message()
            encrypted_message = self.encrypt_message(message)
            api_client.send_group_message(group_id, encrypted_message)
            logger.info("Message sent to group %s: %s", group_id, encrypted_message)
        except Exception as e:
            logger.error("Failed to send message to group %s: %s", group_id, e)