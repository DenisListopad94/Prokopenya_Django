from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Main page")


def rules_page(request):
    return HttpResponse("Rules page")
