from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

# Create your views here.

def index(request):
    return render(request, 'portfoapp/index.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')    
        email = request.POST.get('email')    
        subject = request.POST.get('subject')    
        message = request.POST.get('message') 
        reachout = Message(name=name, email=email, subject=subject, message=message)
        reachout.save() 
        return HttpResponse('Message sent successfully.') 
    return render(request, 'portfoapp/contact.html')


def portfo(request):
    return render(request, 'portfoapp/portfolio.html')

def skill(request):
    return render(request, 'portfoapp/skills.html')


    
