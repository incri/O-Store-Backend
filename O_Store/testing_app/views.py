from django.shortcuts import render
from django.views.decorators.cache import cache_page
import requests
from django.http import HttpResponse
from django.core.cache import cache
from rest_framework.views import APIView




@cache_page(5 * 60)
def say_something(request):
    response = requests.get("https://httpbin.org/delay/2")
    data = response.json()

    return HttpResponse(data)
