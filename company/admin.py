from django.contrib import admin
from .models import State, CompanyType, NoteType

admin.site.register(CompanyType)
admin.site.register(NoteType)
admin.site.register(State)
