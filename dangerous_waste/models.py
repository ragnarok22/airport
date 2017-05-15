from django.db import models

from account.models import Profile


class Waste(models.Model):
    waste = models.CharField('Desecho', max_length=100)
    classification = models.CharField('Clasificacion', max_length=200)
    amount_generated = models.PositiveIntegerField(verbose_name='Cantidad Generada(t)')
    type_condition = models.TextField('Tipo y condiciones de almacenamiento')
    action = models.TextField('Acción de manejo (Clasificación)')
    amount_stored = models.PositiveIntegerField(verbose_name='Cantidad almacenada (t)')
    date_last_measure = models.DateField('Fecha de última medición')
    observations = models.TextField(verbose_name='Observaciones')
    dangerous_waste = models.ForeignKey('DangerousWaste')

    class Meta:
        verbose_name = 'Residuo'
        verbose_name_plural = 'Residuos'

    def __str__(self):
        return self.waste


class DangerousWaste(models.Model):
    airport = models.CharField('Aeropuerto', max_length=200)
    made_by = models.ForeignKey(Profile, verbose_name='Elaborado por')
    date = models.DateField(auto_now=True, verbose_name='Fecha de elaboracion')

    class Meta:
        verbose_name = 'Desecho Peligroso'
        verbose_name_plural = 'Desechos Peligrosos'

    def __str__(self):
        return str(self.date)
