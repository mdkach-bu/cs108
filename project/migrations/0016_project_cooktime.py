# Generated by Django 2.2.7 on 2020-04-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20200424_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cooktime',
            field=models.IntegerField(default=1),
        ),
    ]