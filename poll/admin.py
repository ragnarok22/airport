from django.contrib import admin

from .models import Service, NationalPassengerPoll, InternationalPassengerPoll

admin.site.register(Service)
admin.site.register(NationalPassengerPoll)
admin.site.register(InternationalPassengerPoll)
