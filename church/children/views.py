from django.shortcuts import render
from .models import Children
from django.http import HttpResponse

# Create your views here.

def children_ministry(request):
 children = Children.objects.all()
 return render(request, 'children/children_ministry.html', { 'children': children })
