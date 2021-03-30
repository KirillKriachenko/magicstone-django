from django.shortcuts import render
from django.core.mail import send_mail
from .models import Countertop

# Create your views here.

def show_main_page(request):
    view_template = 'countertops/index.html'

    return render(request,view_template)

def open_contact_form(request):
    view_template = 'countertops/contact.html'

    return render(request,view_template)

def get_all_countertops(request):
    countertops_list = Countertop.objects.all().order_by('-created')
    view_template = 'countertops/countertop-list.html'
    countext = {'countertops':countertops_list}

    return render(request, view_template, countext)


def get_filtered_countertops(request,filter):
    countertops_list = Countertop.objects.filter(category=filter)

    view_template = 'countertops/countertop-list.html'
    countext = {'countertops': countertops_list}

    return render(request,view_template,countext)