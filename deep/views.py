from django.shortcuts import render

def index(request):
    return render(request, 'deep/index.html')

def chat(request):
    return render(request, 'deep/chatdeep.html')
