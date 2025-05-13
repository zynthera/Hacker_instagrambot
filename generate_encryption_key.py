from cryptography.fernet import Fernet
import os

def generate_key(file_name="encryption.key", force=False):
    """
    Generate a secure encryption key and save it to a file.
    """
    try:
        # Check if the file already exists
        if os.path.exists(file_name) and not force:
            print(f"Key file '{file_name}' already exists. Use force=True to overwrite.")
            return
        
        # Generate a new Fernet key
        key = Fernet.generate_key()

        # Save the key to a file
        with open(file_name, "wb") as key_file:
            key_file.write(key)
        
        print(f"Encryption key successfully generated and saved to '{file_name}'.")
    except Exception as e:
        print(f"An error occurred while generating the key: {e}")

if __name__ == "__main__":
    generate_key()
