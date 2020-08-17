"""teachmecpp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from about import views as aboutview
from contribute import views as contributeview
from Algorithm import views as algorithmview
from projects import views as projectsview
from home import views as homeview
from CPP import views as cppview
from DataStructure import views as datastructureview
from Java import views as javaview
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin_content'),
    path('', homeview.home, name = 'home_content'),
    path('projects/', projectsview.projects, name = 'project_content'),
    path('contribute/', contributeview.contribute, name = 'contribute_content'),
    path('about/', aboutview.about, name = 'about_content'),
    
    path('algorithms/', algorithmview.algorithms, name = 'algorithms'),
    path('cpp/', cppview.cpp, name = 'cpp'),
    path('datastructures/', datastructureview.ds, name = 'datastructures'),
    path('java/', javaview.java, name = 'java'),

    re_path(r'^algorithms/(?P<slug>[\w-]+)/$', algorithmview.algorithms_post, name="algorithms_detail"),
    re_path(r'^cpp/(?P<slug>[\w-]+)/$', cppview.cpp_post, name="cpp_detail"),
    re_path(r'^datastructures/(?P<slug>[\w-]+)/$', datastructureview.ds_post, name="datastructure_detail"),
    re_path(r'^java/(?P<slug>[\w-]+)/$', javaview.java_post, name="java_detail")
]

urlpatterns += staticfiles_urlpatterns()