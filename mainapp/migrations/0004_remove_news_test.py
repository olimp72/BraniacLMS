# Generated by Django 3.2 on 2022-09-02 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_news_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='test',
        ),
    ]
