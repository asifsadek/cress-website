from django.db import models
from django_extensions.db.models import TimeStampedModel


class Box(TimeStampedModel):
    cress_space_approved = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{s.description}".format(s=self)

    class Meta:
        verbose_name_plural = 'Boxes'


class Cycle(TimeStampedModel):
    start_date = models.DateTimeField()
    plant = models.TextField()
    box = models.ForeignKey('Box', related_name='cycle')

    def __str__(self):
        return "{s.box} {s.start_date}".format(s=self)


class Photo(TimeStampedModel):
    image = models.ImageField(upload_to='photos', max_length=254)
    owner = models.ForeignKey('auth.User', related_name='image')
    cycle = models.ForeignKey('Cycle', related_name='photo')

    def __str__(self):
        return "{s.image}".format(s=self)


class Sensor(TimeStampedModel):
    sensor_type = models.CharField(max_length=100,
                                   choices=(('DHT22', 'DHT22'), ))
    value_type = models.CharField(max_length=100,
                                  choices=(('temperature', 'temperature [DHT22]'),
                                           ('humidity', 'humidity [DHT22]'), ))
    description = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=100,
                                choices=(('inside', 'inside'),
                                         ('outside', 'outside'), ))
    unit = models.CharField(max_length=100,
                            choices=(('°C', '°C'),
                                     ('%', '%'),
                                     ('Pa', 'Pa'), ))
    value = models.CharField(max_length=255)
    cycle = models.ForeignKey('Cycle', related_name='sensor')

    def __str__(self):
        return "{s.sensor_type} {s.position}".format(s=self)
