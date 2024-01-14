from django.contrib import admin
from .models import Orders
from .models import Requests
from .models import Users

admin.site.register(Orders)
admin.site.register(Requests)
admin.site.register(Users)
# Register your models here.
    