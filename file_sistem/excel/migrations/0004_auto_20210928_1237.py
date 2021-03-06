# Generated by Django 3.2.7 on 2021-09-28 09:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0003_category_subname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='category',
            name='update',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='update',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата изменения'),
        ),
    ]
