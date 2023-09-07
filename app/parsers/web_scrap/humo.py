import requests
from bs4 import BeautifulSoup

from parsers.base_parser import BaseParser


class Humo(BaseParser):
    def __init__(self):
        super().__init__(6, 'https://humo.tj/ru/')

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
            humo_currency = self.soup.find('div', {'class': 'kursHUMO'})
            if humo_currency:
                rates_block = humo_currency.find_all('div', {'class': 'kursBody'})

                if rates_block:
                    for block in rates_block:
                        divs = block.find_all('div')

                        if len(divs) == 3:
                            currency_code = divs[0].text.strip()[2:]
                            currency_id = self._get_currency(currency_code)
                            if currency_id:
                                self.rates.append({
                                    'type_id': 1,
                                    'buy': float(divs[1].text.strip()),
                                    'sell': float(divs[2].text.strip()),
                                    'currency_id': currency_id,
                                })

            if len(self.rates) > 0:
                self._insert_rate()
            return self.rates
        else:
            return 'Soup: no data found'
