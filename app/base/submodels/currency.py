from django.db import models


class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, null=False)
    code = models.SmallIntegerField(null=False)
    symbol = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name
