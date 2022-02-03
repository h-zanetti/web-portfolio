from django.http import HttpResponse
from django.shortcuts import render

def nivana_index(request):
    return render(request, 'core/index.html')