from django.db import models

# Create your models here.
class Countertop(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='assets/')

    #         this.title = title;
    #         this.category = category;
    #         this.description = description;
    #         this.imageUrl = imageUrl;