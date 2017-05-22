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

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.name


def url(self, filename):
    route = 'law/{}/{}'.format(self.register_by, filename)
    return route


def url_analysis(self, filename):
    route = 'analysis/{}/{}'.format(self.make_by, filename)
    return route


class ModelR01PG01(models.Model):
    code = 'R01/PG.190-01'
    area = models.ForeignKey(Area)
    year = models.IntegerField('Año', validators=[validate_year])
    environmental_aspects = models.TextField('Aspectos Ambientales')
    register_by = models.ForeignKey(Profile)
    pub_date = models.DateField('Fecha de publicación', auto_now=True)

    class Meta:
        verbose_name = 'Aspecto Ambiental'
        verbose_name_plural = 'Aspectos Ambientales'

    def __str__(self):
        return "Modelo R01/PG.190-01 {}".format(self.environmental_aspects)


CHARACTER_CHOICES = (
    ('-', 'Negativo'),
    ('+', 'Positivo'),
)


class EnvironmentalAspectMatrix(models.Model):
    code = 'R02/PG.190-01'
    environmental_impact = models.CharField('Impacto Ambiental Asociado', max_length=150)
    activity = models.CharField('Actividad, Producto o servicio', max_length=200)
    consume = models.CharField('Consumo', max_length=100, blank=True)
    frequency = models.PositiveIntegerField('Frecuencia')
    probability = models.PositiveIntegerField('Probabilidad')
    severity = models.PositiveIntegerField('Gravedad')
    character = models.CharField('Caracter', max_length=1, choices=CHARACTER_CHOICES)
    environment_aspect = models.OneToOneField(ModelR01PG01, verbose_name='Aspecto Ambiental')

    class Meta:
        verbose_name = 'Matriz de Aspecto Ambiental'
        verbose_name_plural = 'Matrices de Aspectos Ambientales'

    def __str__(self):
        return self.environmental_impact


class LawRequirement(models.Model):
    code = "PG190-02"
    requirements = models.TextField(verbose_name='Requerimientos')
    law = models.CharField('Ley', max_length=50)
    section = models.CharField('Sección', max_length=100)
    environmental_aspects = models.TextField('Aspectos ambientales')
    file = models.FileField(upload_to=url, blank=True, verbose_name='Fichero')
    register_by = models.ForeignKey(Profile, verbose_name='Registrado por')
    pub_date = models.DateField('Fecha de publicación', auto_now=True)

    class Meta:
        verbose_name = 'Requerimiento Legal'
        verbose_name_plural = 'Requerimientos Legales'

    def __str__(self):
        return '{} {}'.format(self.requirements, self.law)


REPORT_CHOICES = (
    ("e", "Situacion de emergencia"),
    ("a", "Accidente"),
    ("r", "Real"),
    ("s", "Simulacro o Ejercicio"),
)


class EmergencyReport(models.Model):
    code = "PG190-03"
    airport = models.CharField('Aereopuerto', max_length=150)
    no = models.IntegerField('Numero', unique=True)
    report = models.CharField('Reporte', max_length=1, choices=REPORT_CHOICES, default="s")
    datetime = models.DateTimeField(verbose_name='Fecha y hora')
    place = models.CharField(max_length=100, verbose_name='Lugar')
    description = models.TextField(verbose_name='Descripcion')

    class Meta:
        verbose_name = 'Reporte de Emergencia'
        verbose_name_plural = 'Reportes de Emergencia'

    def __str__(self):
        return '{} en {}'.format(self.get_report_display(), self.place)


class Analysis(models.Model):
    make_by = models.ForeignKey(Profile, verbose_name='Elaborado por')
    date = models.DateField(auto_now=True, verbose_name='Fecha de elaboracion')
    summary = models.TextField('Sumario')
    evaluation = models.IntegerField('Evaluacion')
    emergency = models.ForeignKey(EmergencyReport, verbose_name='Reporte de emergencia')

    class Meta:
        verbose_name = 'Analisis'
        verbose_name_plural = 'Analisis'

    def __str__(self):
        return self.summary


class RealAnalysis(Analysis):
    affections = models.TextField('Afectaciones')
    measures = models.TextField('Medidas')
    first_time = models.BooleanField(verbose_name='Es la primera vez', default=False)
    cause = models.TextField('Causa')

    class Meta:
        verbose_name = 'Analisis de Situaciones Reales'
        verbose_name_plural = 'Analisis de una Situacion Real'

    def __str__(self):
        return self.affections


class SimulationAnalysis(Analysis):
    is_necessary_check = models.BooleanField(verbose_name='Es necesario revisar', default=False)
    specify = models.TextField(blank=True, verbose_name='Especificaciones')
    participants = models.FileField(verbose_name='Participantes', blank=True, upload_to=url_analysis)

    class Meta:
        verbose_name = 'Analisis de Simulacro o Ejercicio'
        verbose_name_plural = 'Analisis de Simulacros o Ejercicios'

    def __str__(self):
        return self.specify


COMMUNICATION_CHOICES = (
    ('i', 'interna'),
    ('e', 'externa')
)


class Communication(models.Model):
    airport_name = models.CharField('Nombre del aereopuerto', max_length=100)
    area = models.ForeignKey(Area, verbose_name='Area')
    year = models.IntegerField('Año', validators=[validate_year])
    date = models.DateField('Fecha', auto_now=True)
    reception_way = models.CharField('Via de recepcion', max_length=200)
    type_communication = models.CharField('Tipo de comunicacion', max_length=1, choices=COMMUNICATION_CHOICES)
    contact_data = models.TextField('Datos del contacto')
    info_content = models.TextField('Contenido del la informacion')
    adopted_decision = models.CharField('Decision adoptada', max_length=200)
    distribution_date = models.DateField('Fecha de distribucion')
    emission_path = models.CharField('Via de emision', max_length=200)
    register_by = models.ForeignKey(Profile, verbose_name='Registrado por')

    class Meta:
        verbose_name = 'Comunicacion'
        verbose_name_plural = 'Comunicaciones'

    def __str__(self):
        return '{} {}'.format(self.airport_name, self.type_communication)
