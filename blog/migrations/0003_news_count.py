# Generated by Django 3.0.4 on 2020-03-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200318_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
