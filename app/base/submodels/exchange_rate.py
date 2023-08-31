from django.db import models

from base.submodels.bank import Bank
from base.submodels.currency import Currency
from base.submodels.exchange_rate_type import ExchangeRateType


class ExchangeRate(models.Model):
    id = models.AutoField(primary_key=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    type = models.ForeignKey(ExchangeRateType, on_delete=models.DO_NOTHING, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
    rate = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
