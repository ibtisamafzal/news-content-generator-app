import os
from dotenv import load_dotenv

load_dotenv()

BING_API_KEY = os.getenv("BING_API_KEY")
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")