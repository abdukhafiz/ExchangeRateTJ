import requests

from parsers.base_parser import BaseParser


class Amonat(BaseParser):
    def __init__(self):
        super().__init__(5, 'https://amonatbonk.tj/bitrix/templates/amonatbonk/ajax/ambApi.php')

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
            rates = json['remittances']

            for currency in self.currencies:
                if currency['name'] in rates:
                    item = rates[currency['name']]
                    self.rates.append({
                        'type_id': 1,
                        'buy': float(item['buy']),
                        'sell': float(item['sell']),
                        'currency_id': currency['id'],
                    })

            if len(self.rates) > 0:
                self._insert_rate()
            return self.rates

