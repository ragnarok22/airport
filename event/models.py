from django.db import models


class Event(models.Model):
    date = models.DateField('Fecha')
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descripción', blank=True, null=True)

    class Meta:
        verbose_name = 'Efeméride'
        verbose_name_plural = 'Efemérides'

    def __str__(self):
        return "{} -> {}".format(self.date, self.title)
