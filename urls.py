"""
URL configuration for projectdemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
#from .views import home
from .views import fun2,fun3,fun4
from appdemo.views import appFun2,demo1,disp,dispMarksForm,marksForm
from appdemo.views import appFun

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",demo1,name="homename"),         
    path("url1/",fun2,name="demoname"),
    path("app_url2/",appFun2,name="appFun2Name"),
    path("app_url3/",fun3,name="appFun3Name"),
    path("app_url4/",fun4,name="appFun4Name"),
    path("new/",disp,name="appFun5Name"),
    path("newurl/",appFun,name="appFName"),
    path("newurl2/",marksForm,name="appFun6Nam"),
    path("newurl3/",dispMarksForm,name="appuNam")
    
]



""" configure static and media files to urls """

from django.conf.urls.static import static
from django.conf import  settings


urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)