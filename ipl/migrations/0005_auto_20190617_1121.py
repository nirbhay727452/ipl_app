# Generated by Django 2.2.1 on 2019-06-17 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0004_auto_20190617_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
