from django.shortcuts import render
from .models import Features
# Create your views here.
def index(request):
    posts=Features.objects.all()
    return render(request,'index.html',{'posts':posts})
    