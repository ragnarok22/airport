from django.db import models


class Bulletin(models.Model):
    file = models.FileField()
    title = models.CharField(max_length=150)
    pub_date = models.DateField(auto_now=True)
