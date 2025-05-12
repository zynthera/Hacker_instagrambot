from messaging import MessageHandler
from tasks import TaskManager
from config import Config
from time import sleep

class MockAPIClient:
    def send_group_message(self, group_id, message):
        # Mock sending a message
        print(f"Mock: Sent message to group {group_id}: {message}")

def main():
    api_client = MockAPIClient()
    message_handler = MessageHandler()
    task_manager = TaskManager()

    # Example use case
    while True:
        for group_id in Config.ALLOWED_GROUPS:
            message_handler.send_message(group_id, api_client)
        sleep(Config.MESSAGE_UPDATE_INTERVAL)

if __name__ == "__main__":
    main()