from django.contrib import admin
from.models import Countertop

# Register your models here.
class CountertopAdmin(admin.ModelAdmin):


    fieldsets = [
        ('Countertop', {'fields': ['title', 'category', 'image', 'description']}),
    ]

admin.site.register(Countertop,CountertopAdmin)