from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, world. You're at Django-Reboot home page.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world. You're at Django-Reboot about page.")

def contact(request):
    return HttpResponse("Hello, world. You're at Django-Reboot contact page.")
