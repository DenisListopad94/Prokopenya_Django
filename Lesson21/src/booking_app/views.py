from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Person, Hotels, HotelsComment, User


# Create your views here.
def index(request):
    return render(request=request, template_name="base.html")


def hotels(request):
    hotels_list = [
        {"name": "Happy Hotel", "address": "123 Main Street, Anytown", "stars": 2},
        {"name": "Cozy Cottage Inn", "address": "456 Elm Avenue, Somewhereville", "stars": 1},
        {"name": "Sunset Resort", "address": "789 Beach Road, Paradise City", "stars": 3},
        {"name": "Mountain View Lodge", "address": "101 Pine Lane, Serenity Valley", "stars": 4},
        {"name": "Tranquil Retreat", "address": "555 Lakefront Drive, Peaceful Town", "stars": 5},
    ]
    context = {'hotel_list': hotels_list}

    return render(
        request=request,
        template_name="hotels.html",
        context=context,
    )


def users(request):

    context = {
        'users_list': User.objects.all()
    }

    return render(
        request=request,
        template_name="users.html",
        context=context,
    )


def comments(request):
    users_list = [
        {
            "name": "John",
            "age": 25,
            "comments": ["Great post!", "I totally agree with you."]
        },
        {
            "name": "Alice",
            "age": 30,
            "comments": ["Interesting perspective.", "Nice work!"]
        },
        {
            "name": "Bob",
            "age": 28,
            "comments": ["Thanks for sharing.", "Well written."]
        },
        {
            "name": "Emily",
            "age": 35,
            "comments": ["I have a question.", "This is helpful."]
        },
        {
            "name": "David",
            "age": 22,
            "comments": ["I learned something new.", "Keep up the good work!"]
        },
        {
            "name": "Emma",
            "age": 27,
            "comments": ["Great post!", "I totally agree with you."]
        },
        {
            "name": "Michael",
            "age": 33,
            "comments": ["Interesting perspective.", "Nice work!"]
        },
        {
            "name": "Sophia",
            "age": 29,
            "comments": ["Thanks for sharing.", "Well written."]
        },
        {
            "name": "William",
            "age": 31,
            "comments": ["I have a question.", "This is helpful."]
        },
        {
            "name": "Olivia",
            "age": 26,
            "comments": ["I learned something new.", "Keep up the good work!"]
        }
    ]
    context = {'users_list': users_list}

    return render(
        request=request,
        template_name="comments.html",
        context=context,
    )


def persons(request):
    context = {
        'persons_list': Person.objects.all().prefetch_related("hotel_comments").prefetch_related("hobbies")
    }

    return render(
        request=request,
        template_name="persons.html",
        context=context,
    )


def hotels_view(request):
    context = {
        'hotels_list_view': Hotels.objects.all().prefetch_related("owners").prefetch_related("hotel_comments")
    }

    return render(
        request=request,
        template_name="hotels_view.html",
        context=context,
    )
