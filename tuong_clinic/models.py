"""
tuong_clinic models.
"""
from django.db.models import fields, CharField, DateField, AutoField

from opal import models
from opal.models import ForeignKeyOrFreeText, Title, MaritalStatus, Destination, Gender


class SimplifiedDemographics(models.PatientSubrecord):
    _is_singleton = True
    _icon = 'fa fa-user'

    hospital_number = CharField(
        max_length=255,
        blank=True,
        unique=True,
        help_text="The unique identifier for this patient at the hospital.",
        verbose_name="Mã Số Hồ Sơ"
    )

    name = CharField(max_length=500, blank=True, verbose_name="Tên")
    phone_number = CharField(max_length=255, blank=True, null=True, verbose_name="Số điện thoại")
    date_of_birth = DateField(null=True, blank=True, verbose_name="Ngày sinh")
    address = CharField(max_length=1000, blank=True, null=True, verbose_name="Địa chỉ")
    sex = ForeignKeyOrFreeText(Gender, verbose_name="Giới tính")

    class Meta:
        abstract = True

"""
Core Opal models - these inherit from the abstract data models in
opal.models but can be customised here with extra / altered fields.
"""
class Demographics(SimplifiedDemographics):
    _title = 'Thông Tin'

class Location(models.Location): pass
class Allergies(models.Allergies):
    _title = 'Dị Ứng'
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment):
    _title = 'Điều Trị'

class Investigation(models.Investigation): pass
class SymptomComplex(models.SymptomComplex): pass
class PatientConsultation(models.PatientConsultation): pass
class Notes(models.Notes): pass

# we commonly need a referral route, ie how the patient
# came to the service, but not always.
# class ReferralRoute(models.ReferralRoute): pass

"""
End Opal core models
"""
