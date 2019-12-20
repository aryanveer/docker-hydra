from builtins import dict
from django.views.generic import TemplateView
from .tasks import show_hello_world
from django.http import HttpResponse
from django.shortcuts import render_to_response,render
import requests
import json
# Create your views here.

class ShowHelloWorld(TemplateView):
    template_name='hello_world.html'

    def get(self, *args, **kwargs):
        show_hello_world.apply()
        return super().get(*args, **kwargs)


def home(request,id=None):
    # print("test")
    response = requests.get('http://127.0.0.1:8000/api/?val=dashboard').json()
    # print("test")
    return render(request, 'index.html', response)

