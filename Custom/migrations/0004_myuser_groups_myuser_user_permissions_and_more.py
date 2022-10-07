# Generated by Django 4.0.1 on 2022-10-07 05:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Custom', '0003_alter_transaction_issue_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 7, 11, 21, 39, 276108)),
        ),
    ]
