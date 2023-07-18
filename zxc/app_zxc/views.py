from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')