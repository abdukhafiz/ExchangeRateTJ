from datetime import datetime

from django.db import models

from base.submodels.bank import Bank
from base.submodels.currency import Currency
from base.submodels.rate_type import RateType


class Rate(models.Model):
    id = models.AutoField(primary_key=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    type = models.ForeignKey(RateType, on_delete=models.DO_NOTHING, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
    buy = models.FloatField(null=False)
    sell = models.FloatField(null=False)
    rate_date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'), null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
