# Generated by Django 2.2.1 on 2019-06-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0005_auto_20190617_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='city',
            field=models.CharField(max_length=90, null=True),
        ),
    ]
