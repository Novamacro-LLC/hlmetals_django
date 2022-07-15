from django.db import models
from django_currentuser.db.models import CurrentUserField
from django.utils import timezone


class CompanyType(models.Model):
    company_type_code = models.CharField(max_length=10, null=False)
    company_type_desc = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.company_type_code


class State(models.Model):
    state_name = models.CharField(max_length=25, null=False)
    state_abbr = models.CharField(max_length=2, null=False)

    def __str__(self):
        return self.state_abbr


class Company(models.Model):
    company_type = models.ForeignKey(CompanyType, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, null=False)
    company_address1 = models.CharField(max_length=150, null=False)
    company_address2 = models.CharField(max_length=150, null=True)
    company_city = models.CharField(max_length=50, null=False)
    company_state = models.ForeignKey(State, on_delete=models.CASCADE)
    company_zip = models.CharField(max_length=10, null=False)
    company_phone = models.CharField(max_length=14, null=False)
    company_active = models.BooleanField

    def __str__(self):
        return self.company_name


class NoteType(models.Model):
    note_type_code = models.CharField(max_length=10, null=False)
    note_type_desc = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.note_type_code


class Notes(models.Model):
    note_type = models.ForeignKey(NoteType, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    user = CurrentUserField()
    date_added = models.DateTimeField(default=timezone.now)
    note = models.TextField(null=False)
