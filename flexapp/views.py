from django.shortcuts import render,HttpResponse
from flexapp.models import Login

# Create your views here.

def home(request):
    return render(request, 'home.html')

def detail(request):
    return render(request, 'detail.html')

def product(request):
    return render(request, 'product.html')

def registration(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        login=Login(email=email, password=password)
        login.save()
    return render(request, 'registration.html')

def feed(request):
    return render(request, 'feed.html')