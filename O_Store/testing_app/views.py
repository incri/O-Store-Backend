from django.shortcuts import render
from django.views.decorators.cache import cache_page
import requests
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from rest_framework.views import APIView


class SaySomething(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get("https://httpbin.org/delay/2")
        data = response.json()

        return HttpResponse("ok")
