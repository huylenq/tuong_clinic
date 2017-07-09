# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuong_clinic', '0006_auto_20170709_0330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demographics',
            name='hospital_number',
        ),
        migrations.AddField(
            model_name='demographics',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True),
            preserve_default=False,
        ),
    ]
