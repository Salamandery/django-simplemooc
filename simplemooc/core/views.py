from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {'usuario': 'Momovalda'})

def contact(request):
    return render(request, 'contact.html')