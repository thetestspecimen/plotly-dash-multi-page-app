import os

from dotenv import load_dotenv

load_dotenv()

APP_DEBUG = bool(os.getenv("DEBUG"))
NINJAS_API_KEY = os.getenv("NINJAS_API_KEY")
