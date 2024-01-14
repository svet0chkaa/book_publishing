import random

from django.core import management
from django.core.management.base import BaseCommand
from books_app.models import *
from .utils import random_date, random_timedelta


def add_services():
    Service.objects.create(
        name="Печать",
        description="Для уточнения деталей услуги свяжитесь с нами.",
        price=random.randint(500, 3000),
        image="services/1.jpg"
    )

    Service.objects.create(
        name="Брошюрирование",
        description="Для уточнения деталей услуги свяжитесь с нами.",
        price=random.randint(500, 3000),
        image="services/2.jpg"
    )

    Service.objects.create(
        name="Дизайн обложки",
        description="Для уточнения деталей услуги свяжитесь с нами.",
        price=random.randint(500, 3000),
        image="services/3.jpg"
    )

    Service.objects.create(
        name="Подарок",
        description="Для уточнения деталей услуги свяжитесь с нами.",
        price=random.randint(500, 3000),
        image="services/4.jpg"
    )

    print("Услуги добавлены")


def add_orders():
    users = CustomUser.objects.filter(is_superuser=False)
    moderators = CustomUser.objects.filter(is_superuser=True)

    if len(users) == 0 or len(moderators) == 0:
        print("Заявки не могут быть добавлены. Сначала добавьте пользователей с помощью команды add_users")
        return

    services = Service.objects.all()

    for _ in range(30):
        order = Order.objects.create()
        order.name = "Заказ №" + str(order.pk)
        order.status = random.randint(2, 5)
        order.owner = random.choice(users)
        order.execution_time = random.randint(3, 15)

        if order.status in [3, 4]:
            order.date_complete = random_date()
            order.date_formation = order.date_complete - random_timedelta()
            order.date_created = order.date_formation - random_timedelta()
            order.moderator = random.choice(moderators)
        else:
            order.date_formation = random_date()
            order.date_created = order.date_formation - random_timedelta()

        for i in range(random.randint(1, 3)):
            order.services.add(random.choice(services))

        order.save()

    print("Заявки добавлены")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        management.call_command("clean_db")
        management.call_command("add_users")

        add_services()
        add_orders()









