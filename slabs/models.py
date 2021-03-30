from django.db import models

# Create your models here.
SLAB_MATERIAL_CHOICES = (
    ('quartz', 'Quartz'),
)

SLAB_CATEGORY_CHOICES = (
    ('concrete', 'Concrete'),
    ('calcata', 'Calcata'),
    ('marble', 'Marble'),
    ('exotic', 'Exotic'),
    ('classic', 'Classic'),
    ('sparkling', 'Sparkling'),
)


class Slab(models.Model):

    title = models.CharField(max_length=255)
    slab_material = models.CharField(max_length=255, choices=SLAB_MATERIAL_CHOICES, default='quartz')
    slab_category = models.CharField(max_length=255, choices=SLAB_CATEGORY_CHOICES, default='concrete')
    slab_thikness = models.CharField(max_length=255)
    slab_size = models.CharField(max_length=255)
    slab_finish = models.CharField(max_length=255,blank=True)

    description = models.TextField(blank=True)

    slab_image = models.ImageField(upload_to='static/slabs')
    slab_close_image = models.ImageField(upload_to='static/slabs',blank=True)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SlabWorkExample(models.Model):

    item_ids = models.ForeignKey(Slab, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/slabs')

    created_date = models.DateTimeField(auto_now_add=True)

