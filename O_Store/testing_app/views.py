from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.core.cache import cache


def say_something(request):
    key = "httpbin_result"

    if cache.get(key) is None:
        response = requests.get("https://httpbin.org/delay/2")
        data = response.json()
        cache.set(key, data)
    return HttpResponse(cache.get(key))
