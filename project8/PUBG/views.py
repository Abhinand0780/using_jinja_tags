from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'abi','age':'20'}
    return render(request,'new.html',d)
