# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuong_clinic', '0009_auto_20170709_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='dose',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='drug_fk',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='drug_ft',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='frequency_fk',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='frequency_ft',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='route_fk',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='route_ft',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='start_date',
        ),
        migrations.AddField(
            model_name='treatment',
            name='description',
            field=models.CharField(verbose_name='Mô tả', max_length=10000, blank=True),
        ),
    ]
