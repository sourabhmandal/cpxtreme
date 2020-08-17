from django.shortcuts import render, HttpResponse
from .models import POST, GROUP_TITLE
from home.models import NAV_ITEM

# Create your views here.
def algorithms(request):
    articles = POST.objects.all().order_by('sub_title_no')
    meta_title_list = GROUP_TITLE.objects.all().order_by('title_no')
    nav_item = NAV_ITEM.objects.all().order_by('link_no')
    return render(  request,
                    'algorithms.html', 
                    {   
                        'articles' : articles, 
                        'meta_title_list' : meta_title_list,
                        'nav_item' : nav_item,
                    }
                )
                
def algorithms_post(request, slug):
    article = POST.objects.get(slug=slug)
    all_articles = POST.objects.all().order_by('sub_title_no')
    meta_title = GROUP_TITLE.objects.all().order_by('title_no')
    nav_item = NAV_ITEM.objects.all().order_by('link_no')
    return render(  request, 
                    'articlealgorithms.html', 
                    {'article' : article, 
                    'all_articles' : all_articles, 
                    'meta_title' : meta_title,
                    'nav_item' : nav_item})