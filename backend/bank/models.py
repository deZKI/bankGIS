from django.db import models

CAPABILITY_CHOICES = (
    ('SUPPORTED', 'SUPPORTED'),
    ('UNKNOWN', 'UNKNOWN'),
    ('UNSUPPORTED', 'UNSUPPORTED')
)

ACTIVITY_CHOICES = (
    ('AVAILABLE', 'AVAILABLE'),
    ('UNAVAILABLE', 'UNAVAILABLE'),
    ('UNKNOWN', 'UNKNOWN')
)


class ATMService(models.Model):
    name = models.CharField(verbose_name='Название услуги', max_length=255)
    capability = models.CharField(max_length=60, verbose_name='Возможность оказания услуг', choices=CAPABILITY_CHOICES)
    activity = models.CharField(max_length=60, verbose_name='Доступность услуги в текущий момент времени',
                                choices=ACTIVITY_CHOICES)

    def __str__(self):
        return f"{self.name} - Активность:{self.activity}"
    class Meta:
        verbose_name = 'Сервис АТМ'
        verbose_name_plural = 'Сервисы АТМ'


class ATM(models.Model):
    address = models.CharField(verbose_name='Адрес', max_length=255)
    latitude = models.DecimalField(verbose_name='Широта', max_digits=9, decimal_places=6)
    longitude = models.DecimalField(verbose_name='Долгота', max_digits=9, decimal_places=6)
    allDay = models.BooleanField(verbose_name='Работает круглосуточно')
    services = models.ManyToManyField(ATMService)

    class Meta:
        verbose_name = 'АТМ(банкомат)'
        verbose_name_plural = 'АТМ(банкоматы)'