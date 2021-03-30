from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('',views.get_all_countertops,name='get_all_countertops'),
    path('<filter>',views.get_filtered_countertops,name='get_filtered_countertops')
]