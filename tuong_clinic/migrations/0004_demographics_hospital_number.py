# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuong_clinic', '0003_auto_20170709_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='demographics',
            name='hospital_number',
            field=models.CharField(max_length=255, blank=True, help_text='The unique identifier for this patient at the hospital.'),
        ),
    ]
