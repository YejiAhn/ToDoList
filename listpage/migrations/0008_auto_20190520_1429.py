# Generated by Django 2.1.7 on 2019-05-20 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listpage', '0007_auto_20190520_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='degree',
            field=models.IntegerField(choices=[(1, 'Not Urgent'), (2, 'Intermediate'), (3, 'Urgent')], default=1),
        ),
    ]
