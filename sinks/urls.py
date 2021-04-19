from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('',views.get_all_sinks,name='get_all_sinks'),

]
