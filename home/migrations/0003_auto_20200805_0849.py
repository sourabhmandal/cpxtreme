# Generated by Django 3.1 on 2020-08-05 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_grouptitle_title_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouptitle',
            name='title_no',
            field=models.IntegerField(default=0),
        ),
    ]
