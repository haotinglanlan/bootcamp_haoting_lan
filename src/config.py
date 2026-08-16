import os
from dotenv import load_dotenv


def load_env():
    """Load environment variables from the .env file."""
    load_dotenv()


def get_key():
    """Return the API key stored in the environment."""
    return os.getenv("API_KEY")
