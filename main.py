import os
from dotenv import load_dotenv
from message_generator import generate_group_message
from instagram_api import InstagramAPI
from logger import setup_logger
from rate_limiter import RateLimiter
import asyncio

# Load environment variables
load_dotenv()

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize logger and rate limiter
logger = setup_logger("HackerInstagramBot")
rate_limiter = RateLimiter(rate=10, per=60)  # Limit to 10 requests per minute

async def send_group_message(api, group_id, users):
    """
    Sends personalized messages to all users in a specific group asynchronously.
    """
    for user in users:
        await rate_limiter.wait()  # Enforce rate limiting
        message = generate_group_message(user, GEMINI_API_KEY)
        success = await api.send_message(group_id=group_id, user_id=user, message=message)
        if success:
            logger.info(f"Message sent to @{user} in group {group_id}.")
        else:
            logger.error(f"Failed to send message to @{user}.")

async def main():
    """
    Main logic for logging in to Instagram and sending group messages.
    """
    api = InstagramAPI(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)
    if not await api.login():
        logger.error("Failed to log in. Please check your credentials.")
        return

    groups = await api.fetch_user_groups()
    if not groups:
        logger.error("No groups found where the user is a member.")
        return

    logger.info(f"Logged in successfully as {INSTAGRAM_USERNAME}.")
    for group in groups:
        group_id, group_users = group['id'], group['members']
        logger.info(f"Sending messages to group {group_id}...")
        await send_group_message(api, group_id, group_users)

if __name__ == "__main__":
    asyncio.run(main())