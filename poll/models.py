from django.db import models


EVALUATION_CHOICES = (
    (0, 'No utilizado'),
    (1, 'Malo'),
    (2, 'Insatisfactorio'),
    (3, 'Bueno'),
    (4, 'Muy Bueno'),
    (5, 'Excelente'),
)


services = [
    "Profesionalidad en el chequeo de tráfico.",
    "Profesionalidad del Personal.",
    "Tratamiento dado a sus equipajes.",
    "Disponibilidad de carretillas para equipajes.",
    "Disponibilidad de información.",
    "Limpieza general de la terminal.",
    "Profesionalidad de Agentes de Seguridad",
    "Servicios Gastronómicos.",
    "Sentimiento de seguridad.",
    "Satisfacción general con el aeropuerto.",
    "Transporte desde y hacia la ciudad.",
]


class Service(models.Model):
    title = models.CharField('Servicio', max_length=200)
    evaluation = models.IntegerField('Evaluacion', choices=EVALUATION_CHOICES)
    why = models.TextField(blank=True)
    poll = models.ForeignKey('NationalPassengerPoll', verbose_name='Encuesta a Pasajeros Nacionales')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.title


class NationalPassengerPoll(models.Model):
    opinion = models.TextField('Su opinion')

    class Meta:
        verbose_name = 'Encuesta a Pasajeros Nacionales'
        verbose_name_plural = 'Encuestas a Pasajeros Nacionales'

    def __str__(self):
        return self.opinion

INTERNATIONAL_SERVICES = [
    'Confort en las salas de espera.',
    'Limpieza general de la terminal.',
    'Calidad de los servicios de los baños.',
    'Temperatura en los salones.',
    'Calidad del servicio en las tiendas.',
    'Calidad de los servicios en bares y restaurantes',
    'Facilidad para fumadores.',
    'Disponibilidad de carretillas para equipajes.',
    'Rapidez en la entrega de equipajes al arribar.',
    'Tratamiento dado a sus equipajes.',
    'Disponibilidad de información.',
    'Señalización general.',
    'Profesionalidad en el chequeo de tráfico.',
    'Profesionalidad del personal de Inmigración',
    'Profesionalidad del personal de la Aduana.',
    'Sentimiento de seguridad.',
    'Satisfacción general con el aeropuerto.',
]


class InternationalService(models.Model):
    title = models.CharField('Servicio', max_length=200)
    evaluation = models.IntegerField('Evaluacion', choices=EVALUATION_CHOICES)
    why = models.TextField(blank=True)
    poll = models.ForeignKey('InternationalPassengerPoll', verbose_name='Encuesta a Pasajeros Internacionales')


class InternationalPassengerPoll(models.Model):
    opinion = models.TextField('Su opinion')


class AirLineRepresentPoll(models.Model):
    pass
