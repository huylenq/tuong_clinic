# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuong_clinic', '0007_auto_20170709_0335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demographics',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='marital_status_fk',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='marital_status_ft',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='surname',
        ),
        migrations.AddField(
            model_name='demographics',
            name='name',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
