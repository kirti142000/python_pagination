from django.db import models
from django.utils import timezone
import django

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True , default= django.utils.timezone.now),

    def __str__(self):
      return self.title

