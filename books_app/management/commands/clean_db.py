from django.core.management.base import BaseCommand
from books_app.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Service.objects.all().delete()
        Order.objects.all().delete()
        CustomUser.objects.all().delete()