from django.urls import path
from .views import index, hotels, users, comments
urlpatterns = [
    path('index', index, name="index"),
    path('hotels', hotels, name="hotels"),
    path('users', users, name="users"),
    path('comments', comments, name="comments"),
]
