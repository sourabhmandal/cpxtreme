# Generated by Django 3.1 on 2020-08-10 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Algorithm', '0004_auto_20200809_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_title',
            name='meta_title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
