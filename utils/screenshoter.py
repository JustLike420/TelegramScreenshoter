from typing import Tuple

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


async def take_screenshot(url: str) -> tuple[bool, str]:
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    if 'https://' not in url:
        url = 'https://' + url
    try:
        driver.get(url)
        name = url.replace("https://", "") + ".png"
        driver.save_screenshot(name)
        status = True
    except Exception as e:
        logging.error(e)
        status = False
        name = ''
    return status, name
