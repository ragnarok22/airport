from django.db import models


class Training(models.Model):
    title = models.CharField('Titulo', max_length=100)
    files = models.FileField()
    classes = models.FileField()
    pub_date = models.DateField()
