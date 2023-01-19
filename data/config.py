import os
from dotenv import load_dotenv

load_dotenv()
telegram_token = os.getenv('TELEGRAM_TOKEN')
screenshot_path = os.getenv('SCREEN_PATH')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))