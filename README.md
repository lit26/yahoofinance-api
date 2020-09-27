# yahoofinance-api

python flask api for fetching history and intraday data from yafoo finance.

## API

| HTTP Method | URI | Action|
| ------------- | ------------- | ------------- |
| GET | http://[hostname]/api/[version]/history | get all history stock data (Open, High, Low, Close, Adj Close) |
| GET | http://[hostname]/api/[version]/intraday | get all history stock data (Open, High, Low, Close) |

# Version
v1 history data example: [http://127.0.0.1:5000/api/v1/history?symbol=tsla&start_day=2020-09-14&end_day=2020-09-26&interval=1d](https://raw.githubusercontent.com/lit26/yahoofinance-api/master/sample_data/v1_history.json)

v1 intraday data example: [http://127.0.0.1:5000/api/v1/intraday?symbol=tsla&start_day=2020-09-20&end_day=2020-09-26&interval=1m](https://raw.githubusercontent.com/lit26/yahoofinance-api/master/sample_data/v1_intraday.json)

v2 history data example: [http://127.0.0.1:5000/api/v2/history?symbol=tsla&start_day=2020-09-14&end_day=2020-09-26&interval=1d](https://raw.githubusercontent.com/lit26/yahoofinance-api/master/sample_data/v2_history.json)

v2 intraday data example:[http://127.0.0.1:5000/api/v2/intraday?symbol=tsla&start_day=2020-09-20&end_day=2020-09-26&interval=1m](https://raw.githubusercontent.com/lit26/yahoofinance-api/master/sample_data/v2_intraday.json)

