from django.shortcuts import render

# Create your views here.


def index(request):


    return render(request, "base.html")

def home(request):


    return render(request, "../Model/../templates/index.html")



def contact(request):

    return render(request,'contact.html')

def about(request):

    return render(request,'about.html')