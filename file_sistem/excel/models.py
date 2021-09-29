from django.db import models
from django.utils.timezone import now


class Base(models.Model):
    name = models.CharField('Название', max_length=255, blank=True, null=True)
    create = models.DateTimeField('Дата создания', blank=True, null=True, default=now)
    update = models.DateTimeField('Дата изменения', blank=True, null=True, default=now)
    _create = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(Base):
    subName = models.CharField('Бренд', max_length=255, blank=True, null=True, default='Комфорт')
    path = models.CharField('Путь', max_length=1024, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.subName}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(Base):
    ekd = models.CharField('Документация конструкторов', max_length=1024, blank=True, null=True)
    electricPdf = models.CharField('Электрические схемы', max_length=1024, blank=True, null=True)
    passportPdf = models.CharField('Паспорт', max_length=1024, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'