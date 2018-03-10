import urllib2

import requests
import urllib, json
from pyscraper.selenium_utils import get_headed_driver, wait_for_xpath
from files.downloader import Downloader

# driver = get_headed_driver()
# driver.get('https://www.customink.com/ndx/#/welcome')
# wait_for_xpath(driver, '//*[@id="_08-add-art"]')
# art = driver.find_element_by_xpath('//*[@id="_08-add-art"]')
# art.click()
# wait_for_xpath(driver, '//*[@id="root"]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/section/div/div/div/div/div[1]/div/div/span[1]/div[1]')
# emojis = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/section/div/div/div/div/div[1]/div/div/span[1]/div[1]')
# emojis.click()
# wait_for_xpath(driver, '//*[@id="root"]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/section/div/div/div/ul/li[2]/div')
# smileys = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/section/div/div/div/ul/li[2]/div')
# smileys.click()

categories_json = requests.get('https://www.customink.com/clipart/clipart_categories.json').json()
categories = [(category['id'], '-'.join(category['name'].split('/'))) for category in categories_json[u'_embedded'][u'clipart_categories']]

downloader = Downloader()

all_subcategories = []
for category, name in categories:
    subcategories_json = requests.get('https://www.customink.com/clipart/clipart_categories/{}.json?all=true'.format(category)).json()
    subcategories = [subcategory['id'] for subcategory in subcategories_json['_embedded']['children']]
    # all_subcategories.extend(subcategories)
    for subcategory in subcategories:
        items_json = requests.get('https://www.customink.com/clipart/browse/{}.json'.format(subcategory)).json()
        items = [item['id'] for item in items_json['_embedded']['cliparts']]
        for item in items:
            url = 'https://clipart-manipulate.out.customink.com/prod/manipulate?height=2500&width=2500&red=0&green=0&blue=0&clipart_id={}&path=%2Fclipart%2Feps%2F&fV=false&fH=false&lockRatio=true&transparent=true&grayscale=false&blackwhite=false&rotate=0'.format(item)
            downloader.download_file_category(url, name, item)
        # all_items.extend(items)


# all_items = []
# for subcategory in all_subcategories:
#     items_json = requests.get('https://www.customink.com/clipart/browse/{}.json'.format(subcategory)).json()
#     items = [item['id'] for item in items_json['_embedded']['cliparts']]
#     all_items.extend(items)

# for item in all_items:

print 'h'