"""magicstone URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from countertops import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show_main_page),
    path('contact',views.open_contact_form, name='open_contact_form'),
    # path('countertops/',include('countertops.urls')),
    url(r'^countertops/', include(('countertops.urls', 'countertops'), namespace='countertops')),
    url(r'^slabs/', include(('slabs.urls', 'slabs'), namespace='slabs')),
]
