from django.shortcuts import render

def index(request):
    return render(request, 'mysite/index.html')
# Create your views here.
