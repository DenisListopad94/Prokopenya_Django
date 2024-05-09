from django.db import models


# Create your models here.
class Person(models.Model):
    SEX_PERSON = {
        "m": "male",
        "f": "female",
    }
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=30, null=False)
    sex = models.CharField(max_length=1, choices=SEX_PERSON)
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hobbies = models.ManyToManyField(to="Hobbie")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    photo = models.ImageField(null=True, blank=True)
    id_card_number = models.IntegerField(null=True)
    serial = models.CharField(max_length=30, null=True)
    persons = models.OneToOneField(to="Person", on_delete=models.CASCADE, null=True)
    hotel_owner = models.OneToOneField(to="HotelOwner", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.persons} - {self.serial} - {self.id_card_number}'


class BookInfo(models.Model):
    book_time = models.DateTimeField(auto_now_add=True)
    detail = models.CharField(max_length=200, null=True)
    persons = models.ForeignKey(to="Person", on_delete=models.SET_NULL, null=True)
    hotels = models.ForeignKey(to="Hotels", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.detail}, Person - {self.persons}, {self.book_time}//{self.hotels}'


class Hotels(models.Model):
    name = models.CharField(max_length=50)
    stars = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    rating = models.FloatField(null=True)
    persons = models.ManyToManyField(to="Person")

    def __str__(self):
        return f'{self.name}'


class HotelsComment(models.Model):
    comment = models.CharField(max_length=100)
    time_comment = models.DateTimeField(auto_now_add=True)
    persons = models.ManyToManyField(to="Person")
    hotels = models.ForeignKey(to="Hotels", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.comment}'


class Hobbie(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.name}'


class HotelOwner(models.Model):
    SEX_OWNER = {
        "m": "male",
        "f": "female",
    }
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    experience = models.IntegerField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_OWNER)
    hotels = models.ManyToManyField(to="Hotels")
    hobbies = models.ManyToManyField(to="Hobbie")
