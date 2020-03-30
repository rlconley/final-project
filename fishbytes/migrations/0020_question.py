# Generated by Django 3.0.4 on 2020-03-28 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishbytes', '0019_merge_20200328_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=500)),
                ('pos', models.CharField(blank=True, max_length=5, null=True)),
                ('yesPos', models.CharField(blank=True, max_length=5, null=True)),
                ('noPos', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
    ]
