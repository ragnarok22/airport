from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

SEX_CHOICES = (
    ('M', 'Masculino'),
    ('W', 'Femenino'),
    ('U', 'Sin definir'),
)


def url(self, filename):
    route = 'users/{}/{}'.format(self.username, filename)
    return route


class Profile(User):
    picture = models.ImageField('Imagen', blank=True, null=True, upload_to=url)
    born_date = models.DateField('Fecha de nacimiento', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=SEX_CHOICES, default='U')
    area = models.ForeignKey('model.Area')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def age(self):
        actual = timezone.now().year
        born_year = self.born_date.year
        return actual - born_year

    def set_picture(self, picture):
        self.picture = picture

    def __str__(self):
        return self.get_username()
