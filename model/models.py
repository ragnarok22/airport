from sqlite3 import Date

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from account.models import Profile


def validate_year(value):
    if value > timezone.now().year or value < Date(1900, 1, 1).year:
        raise ValidationError(
            '%(value)s no es un año válido. NOTA: el año debe estar entre 1900 y %(actual_year)s',
            params={'value': value, 'actual_year': timezone.now().year},
        )


class Area(models.Model):
    name = models.CharField('Nombre', max_length=200)

    def __str__(self):
        return self.name


def url(self, filename):
    route = 'law/{}/{}'.format(self.register_by, filename)
    return route


def url_analysis(self, filename):
    route = 'analysis/{}/{}'.format(self.make_by, filename)
    return route


class ModelR01PG01(models.Model):
    area = models.ForeignKey(Area)
    year = models.IntegerField('Año', validators=[validate_year])
    environmental_aspects = models.TextField('Aspectos Ambientales')
    register_by = models.ForeignKey(Profile)
    pub_date = models.DateField('Fecha de publicación', auto_now=True)

    class Meta:
        verbose_name = 'Modelo R01/PG.190-01'
        verbose_name_plural = 'Modelos R01/PG.190-01'

    def __str__(self):
        return "Modelo R01/PG.190-01 {}".format(self.environmental_aspects)


class LawRequirement(models.Model):
    code = "PG190-02"
    requirements = models.TextField(verbose_name='Requerimientos')
    law = models.CharField('Ley', max_length=50)
    section = models.CharField('Sección', max_length=100)
    environmental_aspects = models.TextField('Aspectos ambientales')
    file = models.FileField(upload_to=url, blank=True, verbose_name='Fichero')
    register_by = models.ForeignKey(Profile, verbose_name='Registrado por')
    pub_date = models.DateField('Fecha de publicación', auto_now=True)


REPORT_CHOICES = (
    ("e", "Situacion de emergencia"),
    ("a", "Accidente"),
    ("r", "Real"),
    ("s", "Simulacro o Ejercicio"),
)


class EmergencyReport(models.Model):
    code = "PG190-03"
    no = models.IntegerField('Numero', unique=True)
    report = models.CharField('Reporte', max_length=1, choices=REPORT_CHOICES, default="s")
    datetime = models.DateTimeField(verbose_name='Fecha y hora')
    place = models.CharField(max_length=100, verbose_name='Lugar')
    description = models.TextField(verbose_name='Descripcion')

    def __str__(self):
        return '{} en {}'.format(self.get_report_display(), self.place)


class Analysis(models.Model):
    make_by = models.ForeignKey(Profile, verbose_name='Elaborado por')
    date = models.DateField(auto_now=True, verbose_name='Fecha de elaboracion')
    summary = models.TextField('Sumario')
    evaluation = models.IntegerField('Evaluacion')
    emergency = models.ForeignKey(EmergencyReport, verbose_name='Reporte de emergencia')


class RealAnalysis(Analysis):
    affections = models.TextField('Afectaciones')
    measures = models.TextField('Medidas')
    first_time = models.BooleanField(verbose_name='Es la primera vez', default=False)
    cause = models.TextField('Causa')


class SimulationAnalysis(Analysis):
    is_necessary_check = models.BooleanField(verbose_name='Es necesario revisar', default=False)
    specify = models.TextField(blank=True, verbose_name='Especificaciones')
    participants = models.FileField(verbose_name='Participantes', blank=True, upload_to=url_analysis)
