import requests

from parsers.base_parser import BaseParser


class Arvand(BaseParser):
    def __init__(self):
        super().__init__(8, 'https://arvand.tj/api/currencies/')

    def _fetch_exchange_rate(self):
        try:
            response = requests.get(self.api_url, verify=False)
            print(response.status_code)

            if response.status_code == 200:
                self.response_json = response.json()
            else:
                print('Response code is not 200')
        except Exception as e:
            print(e)

    def parse_rates(self):
        if self.response_json:
            rates = self.response_json

            for rate in rates:
                currency = self._get_currency(rate['currency_name'], False)
                if currency:
                    if rate['type_currency'] == 'TRANSFER_RATE' and rate['currency_name'] == currency['name']:
                        self.rates.append({
                            'type_id': 1,
                            'buy': float(rate['buy_rate']),
                            'sell': float(rate['sell_rate']),
                            'currency_id': currency['id'],
                        })

            if len(self.rates) > 0:
                self._insert_rate()
            return self.rates
