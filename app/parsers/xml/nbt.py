from xml.dom import minidom

import requests

from parsers.base_parser import BaseParser
from utils.helper import Helper


class Nbt(BaseParser):
    def __init__(self):
        helper = Helper()
        today = helper.get_formatted_today()
        super().__init__(3, 'https://nbt.tj/ru/kurs/export_xml.php?date=' + today + '&export=xmlout')

    def _fetch_exchange_rate(self):
        try:
            response = requests.get(self.api_url)

            if response.status_code == 200:
                self.xml_content = response.text
            else:
                print("Failed to fetch the document. Status code:", response.status_code)
                return 'Invalid URL'
        except Exception as e:
            raise Exception('Error on parsing: ' + e)

    def parse_rates(self):
        dom = minidom.parseString(self.xml_content)

        val_curs = dom.getElementsByTagName('ValCurs')[0]
        valutes = val_curs.getElementsByTagName('Valute')

        if len(valutes) > 0:
            for valute in valutes:
                for currency in self.currencies:
                    valute_id = int(valute.getAttribute('ID'))

                    if valute_id == currency['code']:
                        rate = float(valute.getElementsByTagName('Value')[0].firstChild.nodeValue)

                        self.rates.append({
                            'type_id': 2,
                            'buy': rate,
                            'sell': rate,
                            'currency_id': currency['id'],
                        })

            if len(self.rates) > 0:
                self._insert_rate()
            return self.rates
        else:
            return 'No data found'
