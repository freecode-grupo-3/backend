from django.contrib import admin

from backend.models import Disease, ReferenceType

# Register your models here.

admin.site.register(Disease)
admin.site.register(ReferenceType)