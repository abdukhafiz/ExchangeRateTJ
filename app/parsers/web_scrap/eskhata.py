import requests
from bs4 import BeautifulSoup

from parsers.base_parser import BaseParser


class Eskhata(BaseParser):
    def __init__(self):
        super().__init__(1, 'https://eskhata.com')

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
            results = self.soup.find('div', class_='eb-main-cur-rates')
            currency_block = results.find_all('div', class_='only_recent')

            for i, currencyTypes in enumerate(currency_block):
                if i == 2:  # денежные переводы
                    individual_rate = currencyTypes.find_all('tr')

                    for j, rows in enumerate(individual_rate):
                        cols = rows.find_all('td')

                        if len(cols) > 0:
                            if j in [5, 6, 7]:
                                currency = cols[1].text.strip() if cols[1].text.strip() else 0
                                buy = cols[2].text.strip() if cols[2].text.strip() else 0
                                sell = cols[3].text.strip() if cols[3].text.strip() else 0

                                currency_id = self._get_currency(currency)
                                if currency_id:
                                    self.rates.append({
                                        'type_id': 1,
                                        'buy': float(buy.replace(',', '.')),
                                        'sell': float(sell.replace(',', '.')),
                                        'currency_id': currency_id,
                                    })

            if len(self.rates) > 0:
                self._insert_rate()
            return self.rates
        else:
            return 'Soup: no data found'
