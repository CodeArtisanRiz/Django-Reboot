from django.shortcuts import render

# Create your views here.
def all_tea(request):
    return render(request, 'basic/all_tea.html')