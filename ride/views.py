from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def auto(request):
    return HttpResponse('<center><h1>Auto is less cost than cab</h1></center>')
def cab(request):
    return render(request,'cab.html')