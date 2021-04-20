from django.shortcuts import render
from .models import Sink

# Create your views here.
def get_all_sinks(request):
    all_sinks = Sink.objects.all().order_by('-created_date')
    view_template = 'sinks/sink-list.html'
    context = {'sink_list':all_sinks,'filter':'sinks'}

    return render(request,view_template,context)

def get_sink_id(request,sink_id):
    get_sink_id = Sink.objects.get(id=sink_id)
    print(sink_id)
    print(get_sink_id)
    print(get_sink_id.title)
    view_tempalte = 'sinks/sink.html'
    context = {'sink':get_sink_id,'filter':'sinks'}

    return render(request,view_tempalte,context)