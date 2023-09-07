import requests
from bs4 import BeautifulSoup

from parsers.base_parser import BaseParser


class Spitamen(BaseParser):
    def __init__(self):
        super().__init__(4, 'https://www.spitamenbank.tj/ru/personal')

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
            results = self.soup.find('ul', {"id": "currency-list"})
            transfer_rate_block = results.find('li', {'c_index': 3})
            rates = transfer_rate_block.find_all('div', {'class': 'conversation__row'})

            for index, rate in enumerate(rates):
                if index in [1, 2, 3]:
                    conversation_td = rate.find_all('div', {'class': 'conversation__td'})
                    if len(conversation_td) == 3:
                        currency = conversation_td[0]['c-val']
                        buy = conversation_td[1]['c-val']
                        sell = conversation_td[2]['c-val']

                        self.rates.append(
                            {
                                'type_id': 1,
                                'currency_id': self.__get_currency(currency),
                                'buy': buy,
                                'sell': sell
                            }
                        )

            return self.rates

    def __get_currency(self, code):
        return next((currency['id'] for currency in self.currencies if currency['name'] == code), 0)
