from messaging import MessageHandler
from tasks import TaskManager
from config import Config
import logging
from time import sleep

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class MockAPIClient:
    # Mock client for sending messages
    def send_group_message(self, group_id, message):
        logger.info("Mock: Sent message to group %s: %s", group_id, message)

def main():
    api_client = MockAPIClient()
    message_handler = MessageHandler()
    task_manager = TaskManager()

    # Example use case
    logger.info("Bot is starting...")
    try:
        while True:
            for group_id in Config.ALLOWED_GROUPS:
                message_handler.send_message(group_id, api_client)
            sleep(Config.MESSAGE_UPDATE_INTERVAL)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.error("An unexpected error occurred: %s", e)

if __name__ == "__main__":
    main()