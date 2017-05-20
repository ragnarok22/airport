from django.db import models

from account.models import Profile


class Training(models.Model):
    title = models.CharField('Titulo', max_length=100)
    file = models.FileField('Ficheros')
    classes = models.FileField('Ficheros de Clases')
    pub_date = models.DateField('Fecha de publicacion')
    register = models.ManyToManyField(Profile, related_name='register', verbose_name='Registar')

    class Meta:
        verbose_name = 'Capacitacion'
        verbose_name_plural = 'Capacitaciones'
