import json

import requests
from bs4 import BeautifulSoup

from parsers.base_parser import BaseParser


class Imon(BaseParser):
    def __init__(self):
        super().__init__(7, 'https://imon.tj')

    def _fetch_exchange_rate(self):
        try:
            response = requests.get(self.api_url)

            if response.status_code == 200:
                self.soup = BeautifulSoup(response.text, 'html.parser')
            else:
                print('Response code is not 200')
        except Exception as e:
            print(e)

    def parse_rates(self):
        if self.soup:
            app_str = self.soup.find('div', {'id': 'app'})
            if app_str['data-page']:
                json_parsed = json.loads(app_str['data-page'])
                if json_parsed:
                    props = json_parsed['props']
                    if props:
                        rates = props['exchange_rates']

                        if len(rates) > 0:
                            for rate in rates:
                                if rate['rate_buy'] is not None:
                                    currency = self._get_currency(rate['country_code'], False)
                                    if currency:
                                        self.rates.append({
                                            'type_id': 1,
                                            'buy': float(rate['rate_buy']),
                                            'sell': float(rate['rate']),
                                            'currency_id': currency['id'],
                                        })

            if len(self.rates) > 0:
                self._insert_rate()
            return self.rates
        else:
            return 'Soup: no data found'
