from django.contrib import admin
from .models import Person, Profile, Hotels, HotelsComment, HotelOwner, Hobby, BookInfo, User, PersonComment
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]
    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name", "age", "sex"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["city", "email"],
            },
        ),
    ]
    search_fields = ["first_name", "last_name"]
    search_help_text = "Поиск осуществлятся по имени и фамилии, а также email"


admin.site.register(Person)
admin.site.register(Profile)
admin.site.register(Hotels)
admin.site.register(HotelsComment)
admin.site.register(HotelOwner)
admin.site.register(Hobby)
admin.site.register(BookInfo)
admin.site.register(User, UserAdmin)
admin.site.register(PersonComment)

