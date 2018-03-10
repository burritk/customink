import requests
from files.downloader import Downloader

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

print 'h'
