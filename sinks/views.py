from django.shortcuts import render
from .models import Sink

# Create your views here.
def get_all_sinks(request):
    all_sinks = Sink.objects.all()
    view_template = 'sinks/sink.html'
    context = {'sink_list':all_sinks,'filter':'sinks'}

    return render(request,view_template,context)