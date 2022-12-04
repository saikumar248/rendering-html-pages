from django.shortcuts import render


# Create your views here.

def saikumarpages(request):
    return render(request,'home.html')
