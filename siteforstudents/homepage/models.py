from django.db import models

# Create your models here.
class Content(models.Model):
     title = models.CharField(max_length=255)
     content = models.TextField(blank=True)
     file = models.FileField(upload_to='PDF/%Y/%m/%d/')# посмотреть как настроить доступ к pdf
     time_create = models.DateTimeField(auto_now_add=True)
     time_update = models.DateTimeField(auto_now=True)
     is_published = models.BooleanField(default=True)