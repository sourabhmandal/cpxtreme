# Generated by Django 3.1 on 2020-08-06 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200806_0211'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GROUP_TITLE',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='nav_item',
            name='link_no',
            field=models.IntegerField(default=1),
        ),
    ]
