# Generated by Django 3.1 on 2020-08-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='youtube_link',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
