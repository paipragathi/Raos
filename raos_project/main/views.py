from django.shortcuts import render

# main/views.py
from django.shortcuts import render
from .models import Resource

def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'C:/Users/anvit/Projects/RAOS/raos_project/main/templates/main/resource_list.html', {'resources': resources})

