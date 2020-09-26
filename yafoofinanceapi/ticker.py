import re
import json
import datetime
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup

class Ticker:
    def __init__(self):
        self.crumbs = self._get_crumbs()

    def _get_crumbs(self):
        url = 'https://finance.yahoo.com/quote'
        header = {'Connection': 'keep-alive',
                  'Expires': '-1',
                  'Upgrade-Insecure-Requests': '1',
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) \
                           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
                  }

        website = requests.get(url, headers=header)
        soup = BeautifulSoup(website.text, 'lxml')
        crumb = re.findall('"CrumbStore":{"crumb":"(.+?)"}', str(soup))
        return crumb[0]

    def get_data(self, symbol, start_day, end_day, interval='1d'):
        includePrePost = 'true'
        start_day = int(time.mktime(time.strptime(start_day, "%Y-%m-%d")))
        end_day = int(time.mktime(time.strptime(end_day, "%Y-%m-%d")))
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/{}?symbol={}&period1={}&period2={}&interval={}' \
              '&includePrePost={}&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb={}&corsDomain=finance.yahoo.com' \
              ''.format(symbol, symbol, start_day, end_day, interval, includePrePost, self.crumbs)
        response = requests.get(url=url)
        if response.status_code == 200:
            response = json.loads(response.content)
            res_data = response['chart']['result'][0]
            data = res_data['indicators']['quote'][0]
            data['timestamp'] = [datetime.fromtimestamp(i).strftime("%Y-%m-%d") for i in res_data['timestamp']]
            data['adj. close'] = res_data['indicators']['adjclose'][0]['adjclose']
            return data
        else:
            print(response.status_code)
            return None




