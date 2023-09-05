import requests

from parsers.base_parser import BaseParser


class Alif(BaseParser):
    def __init__(self):
        super().__init__(2, 'https://alif.tj/api/rates')

    def _fetch_exchange_rate(self):
        try:
            response = requests.get(self.api_url)

            if response.status_code == 200:
                self.response_json = response.json()
            else:
                print('Response code is not 200')
        except Exception as e:
            print(e)

    def parse_rates(self):
        if self.response_json:
            json = self.response_json
            rates = json['localRates']

            for currency in self.currencies:
                for item in rates:
                    if int(currency['code']) == int(item['currencyCode']):
                        self.rates.append({
                            'type_id': 1,
                            'buy': item['moneyTransferBuyValue'],
                            'sell': item['moneyTransferTradeValue'],
                            'currency_id': currency['id'],
                        })

            if len(self.rates) > 0:
                self._insert_rate()
            return self.rates

