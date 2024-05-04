from django.urls import path
from .views import index, rules_page
urlpatterns = [
    path('index', index),
    path('rules_page', rules_page),
]
