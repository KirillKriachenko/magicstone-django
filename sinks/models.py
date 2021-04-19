from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Sink(models.Model):

    title = models.CharField(max_length=255)
    sink_category = models.CharField(max_length=255)
    sink_image = models.ImageField(upload_to='static/sinks')
    sink_text = RichTextField(blank=True, null=True)

