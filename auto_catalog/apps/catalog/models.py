from django.db import models

# Create your models here.


class Car(models.Model):
    MANUAL, AUTOMATIC, ROBOTIC = range(3)
    TRANSMISSION_CHOICES = [
        [MANUAL, "manual"],
        [AUTOMATIC, "automatic"],
        [ROBOTIC, "robotic"],
    ]

    manufacturer = models.CharField(max_length=30, verbose_name='Производитель')
    model = models.CharField(max_length=30, verbose_name='Модель')
    year = models.PositiveSmallIntegerField(verbose_name='Год выпуска')
    color = models.CharField(max_length=30, verbose_name='Цвет')
    transmission = models.PositiveSmallIntegerField(choices=TRANSMISSION_CHOICES,
                                                    verbose_name='Трансмиссия')

    def __str__(self):
        return f'{self.manufacturer} {self.model} {self.TRANSMISSION_CHOICES[self.transmission][1]} {self.color} {self.year}'

    def get_transmission(self):
        return self.TRANSMISSION_CHOICES[self.transmission][1]

    def get_absolute_url(self):
        return self.pk
