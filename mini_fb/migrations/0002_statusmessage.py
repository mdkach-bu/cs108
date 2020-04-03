# Generated by Django 2.2.7 on 2020-04-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(blank=True)),
                ('profile', models.ForeignKey(on_delete='CASCADE', to='mini_fb.Profile')),
            ],
        ),
    ]
