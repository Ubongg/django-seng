from django.shortcuts import render
from .models import Main
from django.http import HttpResponse

# Create your views here.

def main_church(request):
 mains = Main.objects.all()
 return render(request, 'main/main_church.html', { 'mains': mains })
