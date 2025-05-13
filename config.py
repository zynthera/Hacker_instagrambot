from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

class Config:
    # Instagram API credentials
    INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
    INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
    
    # Encryption settings
    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
    
    # Group permissions (comma-separated group IDs)
    ALLOWED_GROUPS = [group.strip() for group in os.getenv("ALLOWED_GROUPS", "").split(",") if group.strip()]
    
    # Admin contact
    ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "@xploit.ninja")

    # Message update interval (in seconds)
    try:
        MESSAGE_UPDATE_INTERVAL = int(os.getenv("MESSAGE_UPDATE_INTERVAL", "3600"))
    except ValueError:
        logger.error("Invalid MESSAGE_UPDATE_INTERVAL. Falling back to default value of 3600 seconds.")
        MESSAGE_UPDATE_INTERVAL = 3600

    # Validate critical configurations
    @classmethod
    def validate(cls):
        if not cls.INSTAGRAM_USERNAME:
            logger.error("INSTAGRAM_USERNAME is not set in the environment variables.")
        if not cls.INSTAGRAM_PASSWORD:
            logger.error("INSTAGRAM_PASSWORD is not set in the environment variables.")
        if not cls.ENCRYPTION_KEY:
            logger.error("ENCRYPTION_KEY is not set in the environment variables.")
        if not cls.ALLOWED_GROUPS:
            logger.warning("ALLOWED_GROUPS is empty. No groups are authorized to receive messages.")

# Validate configuration on load
Config.validate()