# Generated by Django 4.1.7 on 2023-03-01 03:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blacklist', '0008_alter_blacklist_date_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklist',
            name='date_report',
            field=models.DateField(default=datetime.datetime(2023, 3, 1, 3, 18, 26, 771279, tzinfo=datetime.timezone.utc)),
        ),
    ]
