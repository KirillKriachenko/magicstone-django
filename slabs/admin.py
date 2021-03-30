from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Slab,SlabWorkExample

class SlabWorkInLine(admin.TabularInline):
    model = SlabWorkExample
    extra = 3


# Register your models here.
class SlabAdmin(admin.ModelAdmin):


    fieldsets = [
        ('Slab', {'fields': ['title', 'slab_material', 'slab_category', 'slab_thikness','slab_size','slab_finish','description']}),
        ('Images',{'fields':['slab_image','slab_close_image']})
    ]
    inlines = [SlabWorkInLine]

admin.site.register(Slab,SlabAdmin)