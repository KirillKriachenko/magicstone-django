from django.contrib import admin
from.models import Countertop,Index,IndexImages

# Register your models here.
class IndexImagesInLine(admin.TabularInline):
    model = IndexImages
    extra = 3


class IndexAdmin(admin.ModelAdmin):
    inlines = [IndexImagesInLine]

class CountertopAdmin(admin.ModelAdmin):


    fieldsets = [
        ('Countertop', {'fields': ['title', 'category', 'image', 'description']}),
    ]


admin.site.register(Countertop,CountertopAdmin)
admin.site.register(Index,IndexAdmin)