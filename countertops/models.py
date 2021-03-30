from django.db import models

CATEGORY_CHOICES = (
    ('kitchen','Kitchen'),
    ('vanity', 'Vanity'),
    ('island','Island'),
    ('fireplace','Fireplace'),
    ('custom','Custom'),
)

# Create your models here.
class Countertop(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='kitchen')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='static/countertops')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title