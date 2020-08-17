from django.shortcuts import render

# Create your views here.
def contribute(request):
    return render(request, 'contribute.html')
