from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
     name = models.CharField(
        'Name',blank=False, null=False, max_length=14,db_index=True)
     body = models.CharField(
        'Body',blank=True,null=True,max_length=140,db_index=True)
     created_at = models.DateTimeField(
        'Created DateTime',blank=True,auto_now_add=True)
     like = models.IntegerField('like_count',blank=True,default=0)
     image = CloudinaryField('image',blank=True, null=True)

     def __str__(self):
            return self.name