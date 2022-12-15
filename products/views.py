from django.shortcuts import HttpResponse
import datetime

# Create your views here.

def main(request):
    return HttpResponse("Hello! Its my project")

def goodby(request):
    return HttpResponse("Goodby user")

def now_data(request):
    return HttpResponse(datetime.datetime.now())
