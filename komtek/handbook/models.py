from django.db import models


# Сущность справочник
class Handbook(models.Model):
    title = models.CharField('Наименование', max_length=250, db_index=True)
    short_title = models.CharField('Короткое наименование', max_length=100)
    description = models.TextField('Описание')
    version = models.CharField('Версия', max_length=250)  # unique=True
    date = models.DateField('Дата начала действия справочника этой версии')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'


# Сущность элемент справочника
class Element(models.Model):
    handbook = models.ForeignKey(Handbook, on_delete=models.PROTECT, verbose_name='Родительский идентификатор',
                                 null=True, db_index=True)
    code = models.CharField('Код элемента', max_length=250)
    value = models.CharField('Значение элемента', max_length=250)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'
