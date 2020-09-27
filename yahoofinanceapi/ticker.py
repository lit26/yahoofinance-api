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

    def get_data(self, symbol, start_day, end_day, mode, interval='1d', version='v1'):
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
            if version == 'v1':
                if mode == 'history':
                    data['timestamp'] = [datetime.fromtimestamp(i).strftime("%Y-%m-%d") for i in res_data['timestamp']]
                elif mode == 'intraday':
                    data['timestamp'] = [datetime.fromtimestamp(i).strftime("%Y-%m-%d %H:%M:%S") for i in res_data['timestamp']]

                if mode == 'history':
                    data['adj. close'] = res_data['indicators']['adjclose'][0]['adjclose']
            elif version =='v2':
                if mode == 'history':
                    data = [{'Datetime':datetime.fromtimestamp(res_data['timestamp'][i]).strftime("%Y-%m-%d"),
                         'Open': res_data['indicators']['quote'][0]['open'][i],
                         'High': res_data['indicators']['quote'][0]['high'][i],
                         'Low': res_data['indicators']['quote'][0]['low'][i],
                         'Close':res_data['indicators']['quote'][0]['close'][i],
                         'Adj Close': res_data['indicators']['adjclose'][0]['adjclose'][i]}
                        for i in range(len(res_data['timestamp']))]
                elif mode == 'intraday':
                    data = [{'Datetime': datetime.fromtimestamp(res_data['timestamp'][i]).strftime("%Y-%m-%d %H:%M:%S"),
                             'Open': res_data['indicators']['quote'][0]['open'][i],
                             'High': res_data['indicators']['quote'][0]['high'][i],
                             'Low': res_data['indicators']['quote'][0]['low'][i],
                             'Close': res_data['indicators']['quote'][0]['close'][i]}
                            for i in range(len(res_data['timestamp']))]
            return data

        else:
            if response.status_code == 422:
                response = json.loads(response.content)
                return {'error': response['chart']['error']['description'],'error_code':422}
            else:
                return {'error_code': response.status_code}




