import time

class Cache:
    def __init__(self):
        self.cache = {}

    def set(self, key, value, ttl=None):
        """
        Store a value in the cache with an optional time-to-live (TTL).
        Args:
            key (str): The key for the cached value.
            value (any): The value to be cached.
            ttl (int, optional): Time-to-live in seconds. Defaults to None (no expiration).
        """
        expiry = time.time() + ttl if ttl else None
        self.cache[key] = {"value": value, "expiry": expiry}

    def get(self, key):
        """
        Retrieve a value from the cache.
        Args:
            key (str): The key for the cached value.
        Returns:
            any: The cached value or None if the key does not exist or has expired.
        """
        if key in self.cache:
            entry = self.cache[key]
            if entry["expiry"] is None or entry["expiry"] > time.time():
                return entry["value"]
            else:
                # Remove expired entry
                del self.cache[key]
        return None

    def clear(self):
        """Clear all items in the cache."""
        self.cache.clear()