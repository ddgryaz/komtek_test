# Generated by Django 3.1.3 on 2020-11-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Handbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('short_title', models.CharField(max_length=100, verbose_name='Короткое наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('version', models.CharField(max_length=250, verbose_name='Версия')),
                ('date', models.DateField(verbose_name='Дата начала действия справочника этой версии')),
            ],
        ),
    ]