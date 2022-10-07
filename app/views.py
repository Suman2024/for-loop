from django.shortcuts import render

# Create your views here.
def manimani(request):
    d={'name':'suman','age':22}
    return render(request,'for loop.html',d)