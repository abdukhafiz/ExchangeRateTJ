from django.db import models


class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.name
