# Generated by Django 3.0.5 on 2020-06-15 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200614_0853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезды рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
    ]
