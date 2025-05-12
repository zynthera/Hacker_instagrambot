import os

# Configuration for the bot
class Config:
    # Instagram API credentials
    INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME", "your_username")
    INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD", "your_password")
    
    # Encryption settings
    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "your_encryption_key_here")
    
    # Group permissions (add group IDs here)
    ALLOWED_GROUPS = ["group_id_1", "group_id_2"]

    # Admin contact
    ADMIN_CONTACT = "@xploit.ninja"

    # Message update interval (in seconds)
    MESSAGE_UPDATE_INTERVAL = 3600  # 1 hour