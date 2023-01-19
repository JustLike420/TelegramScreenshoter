import asyncio
from datetime import datetime
import os.path
from selenium import webdriver
import logging
from data.config import screenshot_path, BASE_DIR

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


async def get_filename(url: str):
    import string
    url = url.replace('https://', '')
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in url if c in valid_chars)
    filename = filename.replace(' ', '_')

    now = datetime.now()
    date_now = now.strftime('%Y-%m-%d_%H_%M')

    filename = date_now + '_' + filename + '.png'
    return filename


async def take_screenshot(url: str) -> tuple[bool, str]:
    options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    # options.add_argument('executable_path=drivers/geckodriver.exe')
    driver = webdriver.Firefox(options=options)
    if 'https://' not in url:
        url = 'https://' + url
    try:
        driver.get(url)

        if not os.path.exists(screenshot_path):
            os.mkdir(screenshot_path)

        filename = BASE_DIR + "/" + screenshot_path + "/" + await get_filename(url)
        driver.save_screenshot(filename)
        status = True
    except Exception as e:
        logging.error(e)
        status = False
        filename = ''
    driver.close()
    print(status, filename)
    return status, filename


# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(take_screenshot('https://store.steampowered.com/?l=russian'))
