# Generated by Django 4.1 on 2022-09-22 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Custom', '0002_alter_transaction_issue_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
