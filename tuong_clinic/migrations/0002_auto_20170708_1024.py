# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuong_clinic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demographics',
            name='date_of_death',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='death_indicator',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='ethnicity_fk',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='ethnicity_ft',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='gp_practice_code',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='hospital_number',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='nhs_number',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='post_code',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='religion',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='title_fk',
        ),
        migrations.RemoveField(
            model_name='demographics',
            name='title_ft',
        ),
        migrations.AddField(
            model_name='demographics',
            name='address',
            field=models.CharField(max_length=1000, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='phone_number',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
    ]
