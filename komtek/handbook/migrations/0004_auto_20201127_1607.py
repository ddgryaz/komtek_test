# Generated by Django 3.1.3 on 2020-11-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0003_auto_20201126_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handbook',
            name='title',
            field=models.CharField(db_index=True, max_length=250, verbose_name='Наименование'),
        ),
    ]
