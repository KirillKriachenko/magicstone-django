from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
SINK_CATEGORY = (
    ('undermount', 'Undermount Sink'),
    ('topmount', 'Top-Mount Sink'),
    ('double_bowl', 'Double Bowl Sink'),
    ('sinkgle_bowl', 'Single Bowl Sink'),
    ('porcelain', 'Porcelain Sink'),
)


class Sink(models.Model):

    title = models.CharField(max_length=255)
    sink_category = models.CharField(max_length=255, choices=SINK_CATEGORY,default='undermount')
    sink_image = models.ImageField(upload_to='static/sinks')
    sink_text = RichTextField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

