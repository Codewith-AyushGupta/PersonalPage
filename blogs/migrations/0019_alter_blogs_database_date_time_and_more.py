# Generated by Django 4.0.3 on 2022-05-30 15:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0018_alter_blogs_database_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs_database',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 15, 16, 12, 37196)),
        ),
        migrations.AlterField(
            model_name='blogs_database',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=1),
        ),
        migrations.CreateModel(
            name='BlogComments',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comments', models.TextField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2022, 5, 30, 15, 16, 12, 38881))),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.blogcomments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blogs_database')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
