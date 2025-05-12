import requests

def fetch_random_joke():
    """
    Fetch a random joke from an external joke API.
    Returns:
        str: A joke string containing the setup and punchline.
    """
    try:
        # API endpoint for random jokes
        api_url = "https://official-joke-api.appspot.com/random_joke"
        
        # Make a GET request to fetch the joke
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx or 5xx
        
        # Parse the JSON response
        joke_data = response.json()
        setup = joke_data.get("setup")
        punchline = joke_data.get("punchline")
        
        # Return the formatted joke
        return f"{setup}\n{punchline}"
    except requests.exceptions.RequestException as e:
        # Handle any errors during the API request
        return f"Error fetching joke: {e}"
    except Exception as e:
        # Handle any other unexpected errors
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    # Fetch and display a random joke
    joke = fetch_random_joke()
    print("Here's a random joke for you:")
    print("----------------------------")
    print(joke)