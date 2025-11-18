from django.db import models

# Create your models here.
class Content(models.Model):
     title = models.CharField(max_length=255)
     content = models.TextField(blank=True)
     file = models.FileField(upload_to='PDF/%Y/%m/%d/')# посмотреть как настроить доступ к pdf
     time_create = models.DateTimeField(auto_now_add=True)
     time_update = models.DateTimeField(auto_now=True)
     is_published = models.BooleanField(default=True)
     cat = models.ForeignKey('Category', on_delete=models.PROTECT)

     def __str__(self):
         return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title