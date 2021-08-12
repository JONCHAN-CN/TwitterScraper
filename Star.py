import os
import random
import time
from datetime import datetime as dt
import requests
import shutil

from utils import decorator as dct
from utils import logger, browser

logger = logger.init_logger('./log/star_%s.log' % dt.now().strftime('%Y-%m-%d'))
max_try = 5
dir = './pics/'

@dct.time_elapsed
def scrollToBottom(driver, init_retry=10):
    logger.info('scrolling down to page bottom')
    retry = init_retry

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        SCROLL_PAUSE_TIME = random.randint(1, 2)
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        # dynamic execute
        dynamicGetPics(driver)

        if new_height == last_height:
            if retry < 0:
                break
            else:
                retry = retry - 1
        else:
            last_height = new_height
            retry = init_retry

def dynamicGetPics(driver):
    def _List(trace, mode='xpath'):
        if mode == 'xpath':
            _list = driver.find_elements_by_xpath(trace)
            return _list

    img_urls = _List(trace='//img[@class="css-9pa8cd"]')
    # img_urls = _List(trace='//a[@class="css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1ny4l3l"]') # dynamic load BIG

    for img_url_ele in img_urls:
        try:
            img_url = img_url_ele.get_attribute('src')
            # img_url = img_url_ele.get_attribute('href') # dynamic load BIG
            print(img_url)
            file_name = dir + img_url.split('/')[4].split('?')[0] + '.jpg'
            # file_name = dir + img_url.split('/')[3] + '.jpg' # dynamic load BIG
        except:
            pass
        if os.path.isfile(file_name):
            pass
        else:
            tries = 0
            while True and "media" in img_url:
            # while True : # dynamic load BIG
                tries += 1
                if tries < max_try:
                    try:
                        gallery = requests.get(img_url, stream=True)
                        if gallery.status_code == 200:
                            with open(file_name, 'wb') as fw:
                                shutil.copyfileobj(gallery.raw, fw)
                            print('done getting pics - %d times tried - %s saved' % (tries,file_name))
                            break
                    except:
                        print('trying to get pics - %d times tried' % tries)
                        pass
                else:
                    print('trying to get pics - max tried exceed %d' % max_try)
                    break

def scrapeInfo(driver):
    scrollToBottom(driver)

@dct.time_elapsed
def main():
    # init tw environment
    driver = browser.init_browser(url='https://twitter.com/%s' % target)

    # for first run, login, export
    logger.info("\n请在30秒内完成登录")
    time.sleep(30)
    browser.exp_cookies(driver)

    # for second run and later, import, refresh
    browser.imp_cookies(driver)
    driver.refresh()

    # main function
    scrapeInfo(driver)

    # save cookies
    browser.exp_cookies(driver)

    driver.quit()


if __name__ == "__main__":
    for target in ['TW ACCT HERE PLZ']: # todo alter here
        main()
