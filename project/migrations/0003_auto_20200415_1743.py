# Generated by Django 2.2.7 on 2020-04-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200414_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='instructions',
            field=models.TextField(blank=True),
        ),
    ]
