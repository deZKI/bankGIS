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


class OpeningHours(models.Model):
    days = models.CharField(max_length=2, null=True)  # Например, "пн", "вт", ...
    hours = models.CharField(max_length=50, null=True)  # Например, "10:00-19:00"

    def __str__(self):
        return f'{self.days}: {self.hours}'


class BankBranch(models.Model):
    """ отделение """
    sale_point_name = models.CharField(max_length=255, verbose_name="Название отделения")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    status = models.CharField(max_length=20, verbose_name="Статус", null=True)
    rko = models.CharField(max_length=20, verbose_name="Наличие РКО", null=True)
    office_type = models.CharField(max_length=50, verbose_name="Тип отделения", null=True)
    sale_point_format = models.CharField(max_length=50, verbose_name="Формат отделения", null=True)
    suo_availability = models.CharField(max_length=5, verbose_name="Доступность СУО", null=True)
    has_ramp = models.CharField(max_length=5, verbose_name="Наличие рампы", null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Широта", null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Долгота", null=True)
    metro_station = models.CharField(max_length=255, verbose_name="Ближайшая станция метро", blank=True, null=True)
    distance = models.PositiveIntegerField(verbose_name="Расстояние", null=True)
    kep = models.BooleanField(default=False, verbose_name="КЭП", null=True)
    my_branch = models.BooleanField(default=False, verbose_name="Мой отдел", null=True)
    review_count = models.CharField(max_length=50, verbose_name="Количество отзывов", null=True)
    estimation = models.CharField(max_length=10, verbose_name="Оценка", null=True)

    open_hours = models.ManyToManyField(OpeningHours, related_name="branch_opening_hours", verbose_name="Часы работы")
    open_hours_individual = models.ManyToManyField(OpeningHours, related_name="individual_opening_hours",
                                                   verbose_name="Индивидуальные часы работы")

    def __str__(self):
        return f'Отделение: {self.sale_point_name} - Адресс: {self.address}'

    class Meta:
        verbose_name = 'Отделение банка'
        verbose_name_plural = 'Отделения банков'


class Workload(models.Model):
    """ Загруженность отделения по часам"""
    day = models.CharField(max_length=10, null=True)  # Например, "пн", "вт", ...
    hour = models.CharField(max_length=50, null=True)  # Например, "10:00-19:00"
    people_count = models.PositiveIntegerField()
    branch = models.ForeignKey(to=BankBranch, on_delete=models.CASCADE)

    def __str__(self):
        return f'Время: {self.day} {self.hour} Люди:{self.people_count} Отделение: {self.branch}'


class UserComment(models.Model):
    branch = models.ForeignKey(BankBranch, on_delete=models.CASCADE, related_name="user_comments",
                               verbose_name="Отделение", null=True)
    author = models.CharField(max_length=255, verbose_name="Автор", null=True)
    stars = models.PositiveIntegerField(verbose_name="Оценка", null=True)
    text = models.TextField(verbose_name="Текст комментария", null=True)

    def __str__(self):
        return f'Пользователь: {self.author} - Оценка: {self.stars}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
