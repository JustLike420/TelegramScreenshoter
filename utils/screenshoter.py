from typing import Tuple

from selenium import webdriver
import logging
from data.config import screenshot_path

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
        if not os.path.exists('screenshots'):
            os.mkdir('screenshots')
        now = datetime.now()
        date_now = now.strftime('%Y-%m-%d_%H_%M')
        name = screenshot_path + date_now + '_' + url.replace("https://", "").replace('.', '_') + ".png"
        # driver.save_screenshot(name)
        driver.save_full_page_screenshot(name)
        status = True
    except Exception as e:
        logging.error(e)
        status = False
        name = ''
    driver.close()
    return status, name
