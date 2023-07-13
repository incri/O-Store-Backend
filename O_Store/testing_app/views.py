from django.shortcuts import render
from .tasks import notify_customer
from django.http import HttpResponse

def say_something(request):
    notify_customer.delay('hello')
    return HttpResponse('good')