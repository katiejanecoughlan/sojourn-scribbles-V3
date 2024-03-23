from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def why_ss(request):
    return HttpResponse("Hello, Blog!")