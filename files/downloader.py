import urllib2
import os

import requests


class Downloader:
    def __init__(self):
        self.size = 0

    def download_file_category(self,url, category, file_name):
        file_route = 'pictures/{0}/'.format(category)
        if not os.path.exists(file_route):
            os.makedirs(file_route)
        final_file_name = file_route + str(file_name) + '.png'
        r = requests.get(url)
        headers = r.headers
        file_size = int(headers['content-length'])
        self.size += file_size

        # print "Downloading: %s Bytes: %s" % (file_name, file_size)
        print 'TOTAL({}): '.format(file_route) + str(self.size)

        with open(final_file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

