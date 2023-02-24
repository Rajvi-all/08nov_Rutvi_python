from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def apple(request):
    return render(request,'apple.html')

def sumsang(request):
    return render(request,'sumsang.html')

def vivo(request):
    return render(request,'vivo.html')



