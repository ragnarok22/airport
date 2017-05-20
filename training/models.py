from django.db import models

from account.models import Profile


class Training(models.Model):
    title = models.CharField('Titulo', max_length=100)
    file = models.FileField('Ficheros')
    classes = models.FileField('Ficheros de Clases')
    pub_date = models.DateField('Fecha de publicacion', auto_now=True)
    register = models.ManyToManyField(Profile, related_name='register', verbose_name='Registar', blank=True)

    class Meta:
        verbose_name = 'Capacitacion'
        verbose_name_plural = 'Capacitaciones'

    def __str__(self):
        return self.title
