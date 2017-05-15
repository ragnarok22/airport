from django.contrib import admin

from .models import DangerousWaste, Waste

admin.site.register(Waste)
admin.site.register(DangerousWaste)
