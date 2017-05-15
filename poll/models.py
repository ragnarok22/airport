from django.db import models


EVALUATION_CHOICES = (
    (0, 'No utilizado'),
    (1, 'Malo'),
    (2, 'Insatisfactorio'),
    (3, 'Bueno'),
    (4, 'Muy Bueno'),
    (5, 'Excelente'),
)


class Service(models.Model):
    title = models.CharField('Servicio', max_length=200)
    evaluation = models.IntegerField('Evaluacion', choices=EVALUATION_CHOICES)
    why = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.title


class NationalPassengerPoll(models.Model):
    services = models.ManyToManyField(Service, 'Servicios')
    opinion = models.TextField('Su opinion')
    number = models.PositiveIntegerField('Cantidad de servicios')

    class Meta:
        verbose_name = 'Encuesta a Pasajeros Nacionales'
        verbose_name_plural = 'Encuestas a Pasajeros Nacionales'

    def __str__(self):
        return self.opinion


class InternationalPassengerPoll(models.Model):
    pass


class AirLineRepresentPoll(models.Model):
    pass
