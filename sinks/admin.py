from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Sink

class SinkAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Sink',{'fields': ['title','sink_category','sink_image','sink_text']})
    ]

admin.site.register(Sink,SinkAdmin)