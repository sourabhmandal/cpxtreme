# Generated by Django 3.1 on 2020-08-08 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Java', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='meta_title_no',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Java.group_title'),
        ),
    ]
