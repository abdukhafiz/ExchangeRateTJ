# Generated by Django 3.2.20 on 2023-08-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20230831_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='name',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.SmallIntegerField(),
        ),
    ]
