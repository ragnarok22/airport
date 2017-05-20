from django.core.exceptions import ValidationError
from django.db import models

from account.models import Profile
from model.models import Area

AUDIT_TYPE = (
    ('nc', 'Auditoría Nivel Central'),
    ('sgc', 'Auditoría al SGC'),
    ('z', 'Auditoría de la UEB Aeropuerto'),
    ('sga', 'Auditoría al SGA'),
    ('e', 'Auditoría de la Especialidad (UEB Nacionales)'),
    ('sgi', 'Auditoría al SGICH'),
    ('bv', 'Auditoría de Bureau Veritas'),
    ('ai', 'Auditoría Integrada'),
)


def validate_month(value):
    if value > 12 or value < 1:
        raise ValidationError(
            '%(value)s no es un mes válido. NOTA: el mes debe estar entre 1 y 12',
            params={'value': value},
        )


MONTH = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre',
}


class GeneralProgramAudit(models.Model):
    code = 'R-01/PG.01-05'
    # audit = models.ForeignKey(Audit, verbose_name='Auditoria')
    observations = models.TextField('Observaciones')
    made_by = models.ForeignKey(Profile, verbose_name='Elaborado por')
    date = models.DateField('Fecha', auto_now=True)

    class Meta:
        verbose_name = 'Programa General'
        verbose_name_plural = 'Programas Generales'

    def __str__(self):
        return '{} {}'.format(self.code, self.observations)


class Audit(models.Model):
    area = models.ForeignKey(Area, verbose_name='Area')
    general_program = models.ForeignKey(GeneralProgramAudit, verbose_name='Programa general')
    e = models.CharField('Enero', choices=AUDIT_TYPE, blank=True, max_length=3)
    f = models.CharField('Febrero', choices=AUDIT_TYPE, blank=True, max_length=3)
    ma = models.CharField('Marzo', choices=AUDIT_TYPE, blank=True, max_length=3)
    ab = models.CharField('Abril', choices=AUDIT_TYPE, blank=True, max_length=3)
    m = models.CharField('Mayo', choices=AUDIT_TYPE, blank=True, max_length=3)
    j = models.CharField('Junio', choices=AUDIT_TYPE, blank=True, max_length=3)
    ju = models.CharField('Julio', choices=AUDIT_TYPE, blank=True, max_length=3)
    a = models.CharField('Agosto', choices=AUDIT_TYPE, blank=True, max_length=3)
    s = models.CharField('Septiembre', choices=AUDIT_TYPE, blank=True, max_length=3)
    o = models.CharField('Octubre', choices=AUDIT_TYPE, blank=True, max_length=3)
    n = models.CharField('Noviembre', choices=AUDIT_TYPE, blank=True, max_length=3)
    d = models.CharField('Diciembre', choices=AUDIT_TYPE, blank=True, max_length=3)

    class Meta:
        verbose_name = 'Auditoria'
        verbose_name_plural = 'Auditorias'

    def __str__(self):
        return '{} {}'.format(self.area, self.general_program)


class AuditPlan(models.Model):
    code = 'R-02/PG.01-05'
    pass


class VerifyList(models.Model):
    code = 'R-03/PG.01-05'
    pass


class AuditInform(models.Model):
    code = 'R-04/PG.01-05'
    pass


class AuditControl(models.Model):
    code = 'R-05/PG.01-05'
    pass
