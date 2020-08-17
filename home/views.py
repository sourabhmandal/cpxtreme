from django.shortcuts import render, redirect
from CPP.models import POST, GROUP_TITLE
from .models import NAV_ITEM

# Create your views here.
def home(request):
    return redirect('cpp/')

def home_post(request, slug):
    article = POST.objects.get(slug=slug)
    return render(request, 'article.html', {'article' : article})