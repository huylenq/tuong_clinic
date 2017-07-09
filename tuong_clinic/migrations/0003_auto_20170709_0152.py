# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuong_clinic', '0002_auto_20170708_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demographics',
            name='birth_place_fk',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='birth_place_ft',
        ),
        migrations.AlterField(
            model_name='demographics',
            name='address',
            field=models.CharField(verbose_name='Địa chỉ', max_length=1000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='date_of_birth',
            field=models.DateField(verbose_name='Ngày sinh', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='phone_number',
            field=models.CharField(verbose_name='Số điện thoại', max_length=255, blank=True, null=True),
        ),
    ]
