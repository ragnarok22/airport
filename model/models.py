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


class LawRequirements(models.Model):
    code = "PG190-02"
    requirements = models.TextField()
    law = models.CharField(max_length=50)
    section = models.CharField(max_length=100)
    environmental_aspects = models.TextField()
