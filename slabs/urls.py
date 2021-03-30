from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('<material>', views.get_all_slabs_material, name='get_all_slabs_material'),
    path('<material>/<category>', views.get_material_category_slab, name='get_material_category_slab'),
    path('<material>/<category>/<id>', views.get_countertop_by_id, name='get_countertop_by_id'),

    # path('<filter>',views.get_filtered_countertops,name='get_filtered_countertops')
]
