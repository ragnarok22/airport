from django.contrib import admin

from audit.models import Audit, AuditControl, AuditInform, AuditPlan, GeneralProgramAudit, VerifyList

admin.site.register(Audit)
admin.site.register(AuditControl)
admin.site.register(AuditInform)
admin.site.register(AuditPlan)
admin.site.register(GeneralProgramAudit)
admin.site.register(VerifyList)
