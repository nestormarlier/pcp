from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,'PcpApp/home.html')

def cliente(request):
    return render(request,'PcpApp/cliente.html')

def materiaPrima(request):
    return render(request,'PcpApp/materiaprima.html')

def setup(request):
   return render(request,'PcpApp/setup.html')
    
def fichaTecnica(request):
    return render(request,'PcpApp/fichatecnica.html')