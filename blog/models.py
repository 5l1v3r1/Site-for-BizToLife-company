from django.db import models
from django.shortcuts import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70, db_index=True)
    picture_preview = ProcessedImageField(upload_to='media', format='JPEG', options={'quality': 100})
    slug = models.SlugField(max_length=70, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug':self.slug})

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-date_pub']

class Comment(models.Model):

    name = models.CharField(max_length=30, db_index=True)
    text = models.TextField('Комментарий')
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    date_pub = models.DateTimeField(auto_now_add=True)
    moderation = models.BooleanField('Модерация',default=False)
