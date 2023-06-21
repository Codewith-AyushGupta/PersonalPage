# Generated by Django 4.0.3 on 2022-05-28 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_alter_blogs_database_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs_database',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 6, 17, 7, 250017)),
        ),
        migrations.AlterField(
            model_name='blogs_database',
            name='unique_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]