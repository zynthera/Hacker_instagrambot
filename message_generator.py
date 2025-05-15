import requests
import random

# Predefined fallback messages
fallback_messages = [
    "Access granted. Welcome to the dark side.",
    "System breach detected. Proceed with caution.",
    "Initiating override sequence... Stand by.",
]

def generate_group_message(username, gemini_api_key):
    """
    Generates a personalized message for a user using Gemini AI.
    If Gemini API fails, uses fallback messages.
    """
    try:
        response = requests.post(
            "https://api.gemini.ai/v1/generate",
            headers={"Authorization": f"Bearer {gemini_api_key}"},
            json={"prompt": f"Generate a fun and engaging message for Instagram user @{username}."}
        )
        response.raise_for_status()
        return response.json().get("message", random.choice(fallback_messages))
    except Exception as e:
        print(f"Error using Gemini API: {e}")
        return random.choice(fallback_messages)
