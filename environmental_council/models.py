from django.db import models


class EnvironmentalCouncil(models.Model):
    first_name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellidos', max_length=200)
    position = models.CharField('Cargo', max_length=150)

    class Meta:
        verbose_name = 'Integrante del Consejo Ambiental'
        verbose_name_plural = 'Integrantes del Consejo Ambiental'

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.get_full_name()
