from datetime import datetime

from django.db import models, connection

from django.utils import timezone


class Service(models.Model):
    STATUS_CHOICES = (
        (1, 'Действует'),
        (2, 'Удалена'),
    )

    title = models.CharField(default="Печать", max_length=100, verbose_name="Название")
    status = models.IntegerField(max_length=100, choices=STATUS_CHOICES, default=1, verbose_name="Статус")
    description = models.TextField(default="Описание", max_length=500, verbose_name="Описание")
    price = models.IntegerField(default=1500, verbose_name="Цена")
    image = models.ImageField(upload_to="services", default="services/default.png", verbose_name="Фото")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

    def delete(self):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE books_service SET status = 2 WHERE id = %s", [self.pk])


class Order(models.Model):
    STATUS_CHOICES = (
        (1, 'Введён'),
        (2, 'В работе'),
        (3, 'Завершён'),
        (4, 'Отменён'),
        (5, 'Удалён'),
    )

    book = models.CharField(max_length=100, verbose_name="Книга")
    services = models.ManyToManyField(Service, verbose_name="Выставки", null=True)
    date = models.TimeField(default=datetime.now(tz=timezone.utc), verbose_name="Время")

    status = models.IntegerField(max_length=100, choices=STATUS_CHOICES, default=1, verbose_name="Статус")
    date_created = models.DateTimeField(default=datetime.now(tz=timezone.utc), verbose_name="Дата создания")
    date_of_formation = models.DateTimeField(default=datetime.now(tz=timezone.utc), verbose_name="Дата формирования")
    date_complete = models.DateTimeField(default=datetime.now(tz=timezone.utc), verbose_name="Дата завершения")

    def __str__(self):
        return "Заказ №" + str(self.pk)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"