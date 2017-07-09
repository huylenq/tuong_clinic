# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0029_auto_20170708_1350'),
        ('tuong_clinic', '0010_auto_20170709_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='description',
        ),
        migrations.AddField(
            model_name='treatment',
            name='dose',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='drug_fk',
            field=models.ForeignKey(blank=True, null=True, to='opal.Drug'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='drug_ft',
            field=models.CharField(max_length=255, blank=True, null=True, default=''),
        ),
        migrations.AddField(
            model_name='treatment',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='frequency_fk',
            field=models.ForeignKey(blank=True, null=True, to='opal.Drugfreq'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='frequency_ft',
            field=models.CharField(max_length=255, blank=True, null=True, default=''),
        ),
        migrations.AddField(
            model_name='treatment',
            name='route_fk',
            field=models.ForeignKey(blank=True, null=True, to='opal.Drugroute'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='route_ft',
            field=models.CharField(max_length=255, blank=True, null=True, default=''),
        ),
        migrations.AddField(
            model_name='treatment',
            name='start_date',
            field=models.DateField(blank=True, null=True, help_text='The date on which the patient began receiving this treatment.'),
        ),
    ]
