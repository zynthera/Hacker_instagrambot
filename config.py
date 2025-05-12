from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    # Instagram API credentials
    INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
    INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
    
    # Encryption settings
    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
    
    # Group permissions (comma-separated group IDs)
    ALLOWED_GROUPS = os.getenv("ALLOWED_GROUPS", "").split(",")
    
    # Admin contact
    ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "@xploit.ninja")

    # Message update interval (in seconds)
    MESSAGE_UPDATE_INTERVAL = int(os.getenv("MESSAGE_UPDATE_INTERVAL", "3600"))