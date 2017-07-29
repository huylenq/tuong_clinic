# -*- coding: utf-8 -*-
"""
Defining Opal PatientLists
"""
import datetime

from opal import core
from opal.models import Episode

from tuong_clinic import models


class AllPatientsList(core.patient_lists.PatientList):

    display_name = 'Tất cả'
    slug = 'all_patients'
    allow_add_patient = True

    schema = [
        models.Demographics,
        models.Notes
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()


class DailyList(core.patient_lists.PatientList):

    display_name = 'Hôm nay'
    slug = 'today'
    allow_add_patient = True

    schema = [
        models.Demographics,
        models.Notes
    ]

    def get_queryset(self, **kwargs):
        today = datetime.date.today()
        return Episode.objects.filter(date_of_admission__gte=today)
