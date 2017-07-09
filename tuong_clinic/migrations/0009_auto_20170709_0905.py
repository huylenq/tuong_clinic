# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuong_clinic', '0008_auto_20170709_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='demographics',
            name='hospital_number',
            field=models.CharField(verbose_name='Mã Số Hồ Sơ', max_length=255, unique=True, blank=True, help_text='The unique identifier for this patient at the hospital.'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='name',
            field=models.CharField(verbose_name='Tên', max_length=500, blank=True),
        ),
    ]
