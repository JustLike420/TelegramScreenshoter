import os
from dotenv import load_dotenv

load_dotenv()
telegram_token = os.getenv('TELEGRAM_TOKEN')
admins = os.getenv('ADMINS')
screenshot_path = os.getenv('SCREEN_PATH')

if "," in admins:
    admins = admins.split(",")
else:
    if len(admins) >= 1:
        admins = [admins]
    else:
        admins = []
        print("***** Вы не указали админ ID *****")