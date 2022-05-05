from django.shortcuts import render
from .models import Youth
from django.http import HttpResponse

# Create your views here.

def youth_ministry(request):
 youths = Youth.objects.all()
 return render(request, 'youths/youth_ministry.html', { 'youths': youths })
