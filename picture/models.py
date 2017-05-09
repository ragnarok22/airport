from django.db import models

from account.models import Profile


def url(self, filename):
    route = 'images/{}/{}'.format(self.up_by, filename)
    return route


class Image(models.Model):
    image = models.ImageField('imagen', upload_to=url)
    up_by = models.ForeignKey('subido por', Profile)
    description = models.CharField('descripcion', max_length=100, blank=True)

    def __str__(self):
        return '{} --> {}'.format(self.description, self.up_by)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
