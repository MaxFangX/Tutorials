from django.shortcuts import render
# Might be able to delete the line above
#
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
