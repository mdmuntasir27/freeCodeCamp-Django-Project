from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello world!")

class HelloMoonieBear(View):
    def get(self, request):
        return HttpResponse("Hello Moonie Bear!")