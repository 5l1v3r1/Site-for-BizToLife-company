from django.db import models
from django.shortcuts import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.
class Tool(models.Model):
    title = models.CharField(max_length=70, db_index=True)
    picture_preview = ProcessedImageField(upload_to='media', format='JPEG', options={'quality': 100})
    slide_one = ProcessedImageField(upload_to='media', format='JPEG', options={'quality': 100})
    slide_two = ProcessedImageField(upload_to='media', format='JPEG', options={'quality': 100})
    slide_three = ProcessedImageField(upload_to='media', format='JPEG', options={'quality': 100})
    slide_four = ProcessedImageField(upload_to='media', format='JPEG', options={'quality': 100})
    slug = models.SlugField(max_length=70, unique=True)
    disc = models.CharField(max_length=70)
    tag = models.ManyToManyField('Tag', blank=True, related_name='posts')
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('tool_detail_url', kwargs={'slug':self.slug})

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-date_pub']

class Tag(models.Model):
    title = models.CharField(max_length=15)
    slug = models.SlugField(max_length=15, unique=True)

    def __str__(self):
        return '{}'.format(self.title)
