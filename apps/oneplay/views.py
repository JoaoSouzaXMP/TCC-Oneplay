from django.shortcuts import render

# Create your views here.

def index(request):
   return render(request,'oneplay/index.html')

def info(request):
   return render(request,'oneplay/info.html')

