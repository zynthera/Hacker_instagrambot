import requests
from cache_util import Cache

# Create a cache instance
cache = Cache()

def fetch_random_joke():
    """
    Fetch a random joke from an external joke API.
    Returns:
        str: A joke string containing the setup and punchline.
    """
    # Check if the joke is already cached
    cached_joke = cache.get("random_joke")
    if cached_joke:
        return cached_joke

    api_url = "https://official-joke-api.appspot.com/random_joke"
    retries = 3  # Number of retries for API calls

    for attempt in range(retries):
        try:
            # Make a GET request to fetch the joke
            response = requests.get(api_url, timeout=5)  # Add timeout for better reliability
            response.raise_for_status()  # Raise an error for HTTP codes 4xx or 5xx
            
            # Parse the JSON response
            joke_data = response.json()
            setup = joke_data.get("setup")
            punchline = joke_data.get("punchline")
            
            # Format the joke
            joke = f"{setup}\n{punchline}"

            # Cache the joke with a TTL of 1 hour (3600 seconds)
            cache.set("random_joke", joke, ttl=3600)

            return joke
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1}/{retries} failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    # Return an error message if all retries fail
    return "Error: Unable to fetch a joke after multiple attempts."

if __name__ == "__main__":
    # Fetch and display a random joke
    joke = fetch_random_joke()
    print("Here's a random joke for you:")
    print("----------------------------")
    print(joke)