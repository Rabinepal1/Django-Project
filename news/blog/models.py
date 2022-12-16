from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = RichTextField()

    def __str__(self):
        return self.category_name

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    content = models.TextField()
    page_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class ProjectSettings(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='blog', blank=True, null=True)