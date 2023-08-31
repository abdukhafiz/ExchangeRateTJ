from django.contrib import admin

from base.submodels.bank import Bank
from base.submodels.currency import Currency
from base.submodels.exchange_rate import ExchangeRate
from base.submodels.exchange_rate_type import ExchangeRateType

admin.site.register(Bank)
admin.site.register(Currency)
admin.site.register(ExchangeRateType)
# admin.site.register(ExchangeRate)
