import requests
from files.downloader import Downloader

categories_json = requests.get('https://www.customink.com/clipart/clipart_categories.json').json()
categories = [(category['id'], '-'.join(category['name'].split('/'))) for category in categories_json[u'_embedded'][u'clipart_categories']]

downloader = Downloader()

all_subcategories = []
counter = 0
for category, name in categories:
    subcategories_json = requests.get('https://www.customink.com/clipart/clipart_categories/{}.json?all=true'.format(category)).json()
    subcategories = [subcategory['id'] for subcategory in subcategories_json['_embedded']['children']]
    # all_subcategories.extend(subcategories)
    for sindex, subcategory in enumerate(subcategories):
        try:
            items_json = requests.get('https://www.customink.com/clipart/browse/{}.json'.format(subcategory)).json()
            items = [item['id'] for item in items_json['_embedded']['cliparts']]
            for index, item in enumerate(items):
                try:
                    print '{0}/{1} C, {2}/{3} SC, {4}/{5} I'.format(counter, len(categories), sindex, len(subcategories), index, len(items)),
                    url = 'https://clipart-manipulate.out.customink.com/prod/manipulate?height=2500&width=2500&red=0&green=0&blue=0&clipart_id={}&path=%2Fclipart%2Feps%2F&fV=false&fH=false&lockRatio=true&transparent=true&grayscale=false&blackwhite=false&rotate=0'.format(item)
                    downloader.download_file_category(url, name, item)
                except:
                    print 'Skipped item'
                    continue
        except:
            print 'Skipped subcategory'
            continue
        # all_items.extend(items)
    counter += 1

print 'h'
