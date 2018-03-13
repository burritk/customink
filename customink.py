import requests
from files.downloader import Downloader
import sys

categories_json = requests.get('https://www.customink.com/clipart/clipart_categories.json').json()
categories = [(category['id'], '-'.join(category['name'].split('/'))) for category in categories_json[u'_embedded'][u'clipart_categories']]

downloader = Downloader()
res = '2500'
category_start = 0
subcategory_start = 0
item_start = 0
try: res = sys.argv[1]
except: pass
try: category_start = sys.argv[2]
except: pass
try: subcategory_start = sys.argv[3]
except: pass
try: item_start = sys.argv[4]
except: pass
print 'Downloading files in {0}x{1} resolution'.format(res, res)

all_subcategories = []
category_counter = category_start
for category, name in categories[category_start:]:
    subcategories_json = requests.get('https://www.customink.com/clipart/clipart_categories/{}.json?all=true'.format(category)).json()
    subcategories = [subcategory['id'] for subcategory in subcategories_json['_embedded']['children']]
    # all_subcategories.extend(subcategories)
    subcategory_counter = subcategory_start
    for subcategory in subcategories[subcategory_start:]:
        try:
            items_json = requests.get('https://www.customink.com/clipart/browse/{}.json'.format(subcategory)).json()
            items = [item['id'] for item in items_json['_embedded']['cliparts']]
            item_counter = item_start
            for item in items[item_start:]:
                try:
                    print '{0}/{1} C, {2}/{3} SC, {4}/{5} I'.format(category_counter, len(categories), subcategory_counter, len(subcategories), item_counter, len(items)),
                    url = 'https://clipart-manipulate.out.customink.com/prod/manipulate?height={0}&width={1}&red=0&green=0&blue=0&clipart_id={2}&path=%2Fclipart%2Feps%2F&fV=false&fH=false&lockRatio=true&transparent=true&grayscale=false&blackwhite=false&rotate=0'.format(res, res, item)
                    downloader.download_file_category(url, name, item)
                except:
                    print 'Skipped item'
                    continue
            item_start = 0
        except:
            print 'Skipped subcategory'
            continue
        # all_items.extend(items)
    subcategory_start = 0
    category_counter += 1

print 'Done.'
