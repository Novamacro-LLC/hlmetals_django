from django import forms
from .models import Company


class Customer(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name',
                  'company_address1',
                  'company_address2',
                  'company_city',
                  'company_state',
                  'company_zip',
                  'company_phone')


class Recycler(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name',
                  'company_address1',
                  'company_address2',
                  'company_city',
                  'company_state',
                  'company_zip',
                  'company_phone')


class Trucking(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name',
                  'company_address1',
                  'company_address2',
                  'company_city',
                  'company_state',
                  'company_zip',
                  'company_phone')


class Vendor(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name',
                  'company_address1',
                  'company_address2',
                  'company_city',
                  'company_state',
                  'company_zip',
                  'company_phone')
