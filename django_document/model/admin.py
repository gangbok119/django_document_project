from django.contrib import admin

# Register your models here.
from .models import (
    Person,
    User,
    Car,
    Manufacturer,
    Pizza,
    Topping,
    TwitterUser,
    InstagramUser,
    Idol,
    Group,
    Membership,
    Place,
    Restaurant,
)

admin.site.register(Person)
admin.site.register(User)
admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(TwitterUser)
admin.site.register(InstagramUser)
admin.site.register(Idol)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Place)
admin.site.register(Restaurant)