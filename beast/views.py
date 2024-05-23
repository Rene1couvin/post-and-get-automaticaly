
from django.shortcuts import render
from .models import *

def index(request):
    record =Info.objects.all()
    context = {
        "records": record
    }
    if request.method == "POST":
        info = Info()
        info.name = request.POST['name']
        info.email = request.POST['email']
        info.phone = request.POST['phone']
        info.work = request.POST['work'] 
        info.save()

    return render(request, "profiling.html", context)
