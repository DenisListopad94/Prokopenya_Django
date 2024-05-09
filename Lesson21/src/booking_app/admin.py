from django.contrib import admin
from .models import Person, Profile, Hotels, HotelsComment, HotelOwner, Hobbie, BookInfo
# Register your models here.

admin.site.register(Person)
admin.site.register(Profile)
admin.site.register(Hotels)
admin.site.register(HotelsComment)
admin.site.register(HotelOwner)
admin.site.register(Hobbie)
admin.site.register(BookInfo)

