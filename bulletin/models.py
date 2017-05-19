from django.db import models


class Bulletin(models.Model):
    title = models.CharField('Titulo', max_length=150)
    file = models.FileField('PDF')
    pub_date = models.DateField('Fecha de Publicacion', auto_now=True)

    class Meta:
        verbose_name = 'Boletin'
        verbose_name_plural = 'Boletines'

    def __str__(self):
        return '{} {}'.format(self.title, self.pub_date)
