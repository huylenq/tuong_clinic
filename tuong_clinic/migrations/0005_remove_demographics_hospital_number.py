# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuong_clinic', '0004_demographics_hospital_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demographics',
            name='hospital_number',
        ),
    ]
