from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('',views.get_all_sinks,name='get_all_sinks'),
    path('<sink_id>',views.get_sink_id,name='get_sink_id'),

]
