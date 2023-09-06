from base.submodels.currency import Currency
from base.submodels.rate import Rate
from utils.helper import Helper


class BaseParser:
    def __init__(self, bank_id, api_url):
        self.bank_id = bank_id
        self.api_url = api_url

        self.currencies = self.__get_currencies()
        self.rates = []

        self._fetch_exchange_rate()

    def _fetch_exchange_rate(self):
        pass

    def _insert_rate(self):
        helper = Helper()
        today = helper.get_formatted_today()
        for item in self.rates:
            created = Rate.objects.update_or_create(
                bank_id=self.bank_id,
                buy=item['buy'],
                sell=item['sell'],
                currency_id=item['currency_id'],
                type_id=item['type_id'],
                rate_date=today,
                defaults={
                    'buy': item['buy'],
                    'sell': item['sell'],
                    'rate_date': today
                }
            )

            # TODO: Log created item (created variable)

    def __get_currencies(self, ignore_tjs=True):
        if ignore_tjs:
            return Currency.objects.exclude(name='TJS').values()
        return Currency.objects.all().values()
