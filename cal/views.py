from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calc(request):
    return render(request,'calc.html')

def gopal(request):
    return HttpResponse('<h1>hi gopal</h1>')
