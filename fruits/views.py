from django.shortcuts import render

# Create your views here.

def apple(request):
    return render(request,"apple.html")

def graphs(request):
    return render(request,"graphs.html")