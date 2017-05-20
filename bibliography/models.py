from django.db import models

DOCUMENT_TYPE_CHOICES = (
    ('CGA', 'Consejo de Gestion Ambiental'),
    ('Otros', 'Otros Documentos'),
)


class Bibliography(models.Model):
    document_type = models.CharField('Tipo de documento', max_length=5, choices=DOCUMENT_TYPE_CHOICES)
    pub_date = models.DateField(auto_now=True)
    file = models.FileField('Fichero')

    class Meta:
        verbose_name = 'Bibliografia'
        verbose_name_plural = 'Bibliografias'

    def __str__(self):
        return '{} {}'.format(self.document_type, self.file)
