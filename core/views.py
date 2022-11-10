from django.shortcuts import render

# Create your views here.
def sayt(request):
    return render(request , 'index.html')