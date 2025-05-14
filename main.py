import os
import asyncio
from dotenv import load_dotenv
from message_generator import generate_group_message
from instagram_api import InstagramAPI
from rate_limiter import RateLimiter
from logger import logger

# Load environment variables from .env
load_dotenv()

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # For Gemini AI API

rate_limiter = RateLimiter(rate_limit=10, time_window=60)  # Max 10 messages per 60 seconds

async def send_group_message(api, group_id, users):
    """
    Sends personalized messages to all users in a specific group.
    Implements rate limiting to avoid being flagged by Instagram.
    """
    for user in users:
        if rate_limiter.is_allowed():
            # Generate message using Gemini AI
            message = generate_group_message(user, GEMINI_API_KEY)
            success = await api.send_message(group_id=group_id, user_id=user, message=message)
            if success:
                logger.info(f"Message sent to @{user} in group {group_id}.")
            else:
                logger.error(f"Failed to send message to @{user} in group {group_id}.")
        else:
            logger.warning("Rate limit exceeded. Waiting...")
            await asyncio.sleep(rate_limiter.time_to_reset())

async def main():
    """
    Main function to log in to Instagram and send messages to groups.
    """
    api = InstagramAPI(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)
    logged_in = await api.login()
    if not logged_in:
        logger.error("Failed to log in to Instagram. Please check credentials.")
        return

    groups = await api.fetch_user_groups()
    if not groups:
        logger.warning("No groups found where the user is a member.")
        return

    for group in groups:
        group_id = group['id']
        group_users = group['members']
        await send_group_message(api, group_id, group_users)

if __name__ == "__main__":
    asyncio.run(main())