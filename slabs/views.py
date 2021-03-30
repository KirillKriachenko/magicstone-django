from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .models import Slab, SlabWorkExample
# Create your views here.


def get_all_slabs_material(request,material):
    print(material)
    slabs_list = Slab.objects.filter(slab_material=material).order_by('-created_date')
    print(slabs_list)
    view_template = 'slabs/slab-list.html'
    context = {'slabs':slabs_list}

    return render(request,view_template,context)

def get_material_category_slab(request,material,category):
    slab_list = Slab.objects.filter(slab_material=material,slab_category=category).order_by('-created_date')
    view_template = 'slabs/slab-list.html'
    context = {'slabs':slab_list}

    return render(request,view_template,context)

def get_countertop_by_id(request,material,category,id):
    view_template = 'slabs/slab.html'

    if request.method == 'POST':
        message_name = request.POST.get('name', '')
        message_email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # print(message_name)
        # return render(request, view_template, {'message_name': message_name})

        if message_name and message and message_email:
            try:
                send_mail('Sent from site', message, message_email, ['info@magicstone.ca'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request,view_template,{'message_name':message_name})

        # message_name = request.POST['name']
        # message_email = request.POST['email']
        # message = request.POST['message']
        #
        # print(message_name)
        #
        # send_mail(
        #     'Message from site', #subject
        #     message, #message
        #     message_email, # from Email
        #     ['info@magicstone.ca'], #To Email
        # )

    slab_ids = Slab.objects.get(id=id)
    slab_works = SlabWorkExample.objects.filter(item_ids=id)

    # print(material)
    # print(id)
    context = {'slab':slab_ids, 'slab_works':slab_works}

    return render(request,view_template,context)