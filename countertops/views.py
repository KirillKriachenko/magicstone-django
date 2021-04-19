from django.shortcuts import render
from django.core.mail import send_mail
from .models import Countertop,IndexImages

# Create your views here.

def show_main_page(request):
    index_images = IndexImages.objects.filter(index_ids=1)
    view_template = 'countertops/index.html'
    print(index_images)
    context = {'images':index_images}

    return render(request,view_template,context)

def open_contact_form(request):
    view_template = 'countertops/contact.html'

    return render(request,view_template)

def get_all_countertops(request):
    countertops_list = Countertop.objects.all().order_by('-created')
    view_template = 'countertops/countertop-list.html'
    countext = {'countertops':countertops_list,'filter':'all','link':'countertops'}

    return render(request, view_template, countext)


def get_filtered_countertops(request,filter):
    countertops_list = Countertop.objects.filter(category=filter)

    view_template = 'countertops/countertop-list.html'
    countext = {'countertops': countertops_list,'filter':filter,'link':'countertops'}

    return render(request,view_template,countext)

def get_about_page(request):
    view_template = 'countertops/about.html'
    return render(request,view_template)