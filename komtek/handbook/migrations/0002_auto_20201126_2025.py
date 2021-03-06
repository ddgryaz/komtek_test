# Generated by Django 3.1.3 on 2020-11-26 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='handbook',
            options={'verbose_name': 'Справочник', 'verbose_name_plural': 'Справочники'},
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250, verbose_name='Код элемента')),
                ('value', models.CharField(max_length=250, verbose_name='Значение элемента')),
                ('r_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='handbook.handbook')),
            ],
            options={
                'verbose_name': 'Элемент',
                'verbose_name_plural': 'Элементы',
            },
        ),
    ]
