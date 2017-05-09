from django.db import models

from account.models import Profile


def url(self, filename):
    route = 'images/{}/{}'.format(self.up_by, filename)
    return route


class Image(models.Model):
    image = models.ImageField(upload_to=url)
    up_by = models.ForeignKey(Profile)
