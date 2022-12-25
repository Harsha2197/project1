from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Home(request):
    return HttpResponse('status-200')

def index(request):
    return render(request,'index.html')