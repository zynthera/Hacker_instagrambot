import os
from dotenv import load_dotenv
from message_generator import generate_group_message
from instagram_api import InstagramAPI

# Load environment variables from .env
load_dotenv()

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

def login_and_fetch_groups():
    """
    Logs in to Instagram and fetches groups where the user is a member.
    """
    api = InstagramAPI(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)
    if not api.login():
        print("Failed to log in. Please check your credentials in the .env file.")
        return None, None

    groups = api.fetch_user_groups()
    if not groups:
        print("No groups found where the user is a member.")
        return api, None

    print(f"Logged in successfully as {INSTAGRAM_USERNAME}.")
    return api, groups

def send_group_message(api, group_id, users):
    """
    Sends personalized messages to all users in a specific group.
    """
    for user in users:
        message = generate_group_message(user)
        if api.send_message(group_id=group_id, user_id=user, message=message):
            print(f"Message sent to @{user} in group {group_id}.")
        else:
            print(f"Failed to send message to @{user}.")

if __name__ == "__main__":
    api, user_groups = login_and_fetch_groups()

    if user_groups:
        # Example: Sending a message to the first group
        group_id, group_users = user_groups[0]['id'], user_groups[0]['members']
        send_group_message(api, group_id, group_users)