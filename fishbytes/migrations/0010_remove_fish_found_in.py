# Generated by Django 3.0.4 on 2020-03-26 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishbytes', '0009_auto_20200326_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish',
            name='found_in',
        ),
    ]
