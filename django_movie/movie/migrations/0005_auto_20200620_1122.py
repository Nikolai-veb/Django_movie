# Generated by Django 3.0.5 on 2020-06-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20200615_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='actor',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='actor',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='actor',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='category',
            name='discription_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='discription_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='ganre',
            name='discription_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='ganre',
            name='discription_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='ganre',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='ganre',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='movie',
            name='country_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='movie',
            name='country_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Опискние'),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Опискние'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tagline_en',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Слоган'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tagline_ru',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Слоган'),
        ),
        migrations.AddField(
            model_name='movie',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='movie',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='movieshots',
            name='discriprion_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='movieshots',
            name='discriprion_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='movieshots',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='movieshots',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
    ]
