from django.shortcuts import render
from django .http import HttpResponse

# Create your views here.
def veg(request):
    return HttpResponse('<h1>Vegetarian<masquree> Idly,Sambhar,Vada,Poori</masquree> </h1>')
def nonveg(request):
    return render(request,'nonveg.html')
