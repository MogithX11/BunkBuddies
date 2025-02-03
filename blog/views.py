from django.shortcuts import render
from django.http import HttpResponse 
def home(request):
    return HttpResponse('<h1>Home</h1>')
    return render(request, 'blog/home.html')

def about(request):
    return HttpResponse('<h1>About Us<h1>')

def login(request):
    return render()
