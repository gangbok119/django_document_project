from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Person)
admin.site.register(User)
admin.site.register(Car)
admin.site.register(Manufacturer)