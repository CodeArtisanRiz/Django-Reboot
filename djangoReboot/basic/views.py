from django.shortcuts import render
from .models import TeaTypes

# Create your views here.
def all_tea(request):
    teas = TeaTypes.objects.all()
    return render(request, 'basic/all_tea.html', {'teas': teas})