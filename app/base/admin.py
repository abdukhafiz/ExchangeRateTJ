from django.contrib import admin

from base.submodels.bank import Bank
from base.submodels.currency import Currency
from base.submodels.rate import Rate
from base.submodels.rate_type import RateType

admin.site.register(Bank)
admin.site.register(Currency)
admin.site.register(RateType)
# admin.site.register(ExchangeRate)
