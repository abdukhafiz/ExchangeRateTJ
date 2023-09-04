from base.submodels.currency import Currency
from base.submodels.rate import Rate


class BaseApiParser:
    def __init__(self, bank_id, rate_api):
        self.bank_id = bank_id
        self.rate_api = rate_api

        self.currencies = self.__get_currencies()
        self.response_json = {}
        self.rates = []

    def _insert_rate(self):
        for item in self.rates:
            created = Rate.objects.update_or_create(
                bank_id=self.bank_id,
                buy=item['buy'],
                sell=item['sell'],
                currency_id=item['currency_id'],
                type_id=item['type_id'],
                defaults={
                    'buy': item['buy'],
                    'sell': item['sell']
                }
            )

            # TODO: Log created item (created variable)

    def __get_currencies(self, ignore_tjs=True):
        if ignore_tjs:
            return Currency.objects.exclude(name='TJS').values()
        return Currency.objects.all().values()
