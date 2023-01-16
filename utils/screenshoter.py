from typing import Tuple

from selenium import webdriver
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


async def take_screenshot(url: str) -> tuple[bool, str]:
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument('executable_path=drivers/geckodriver.exe')
    driver = webdriver.Firefox(options=options)
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
    driver.close()
    return status, name
