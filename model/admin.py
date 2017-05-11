from django.contrib import admin

from model.models import Area, ModelR01PG01, LawRequirement, EmergencyReport, RealAnalysis, SimulationAnalysis, \
    Communication

admin.site.register(Area)
admin.site.register(ModelR01PG01)
admin.site.register(LawRequirement)
admin.site.register(EmergencyReport)
admin.site.register(RealAnalysis)
admin.site.register(SimulationAnalysis)
admin.site.register(Communication)
