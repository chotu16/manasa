from django.shortcuts import render
from django.http import httpResponse
# Create your views here.

def hello(request):
 return httpResponse('hi')