from django.shortcuts import render
from .models import POST, GROUP_TITLE
from home.models import NAV_ITEM

# Create your views here.
def java(request):
    articles = POST.objects.all().order_by('sub_title_no')
    meta_title_list = GROUP_TITLE.objects.all().order_by('title_no')
    nav_item = NAV_ITEM.objects.all().order_by('link_no')
    return render(  request,
                    'java.html', 
                    {'articles' : articles, 
                    'meta_title_list' : meta_title_list,
                    'nav_item' : nav_item}
                )

def java_post(request, slug):
    article = POST.objects.get(slug=slug)
    all_articles = POST.objects.all().order_by('sub_title_no')
    meta_title = GROUP_TITLE.objects.all().order_by('title_no')
    nav_item = NAV_ITEM.objects.all().order_by('link_no')
    return render(  request, 
                    'articlejava.html', 
                    {'article' : article,
                    'all_articles' : all_articles,
                    'meta_title' : meta_title,
                    'nav_item' : nav_item}
                )