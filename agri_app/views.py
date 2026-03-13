from django.shortcuts import render

def home(request):
    return render(request, 'frontend/index.html')

def contact(request):
    return render(request, 'frontend/contact.html')

def farmers(request):
    return render(request, 'frontend/farmers.html')
