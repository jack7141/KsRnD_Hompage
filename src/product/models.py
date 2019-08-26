from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    overview_images = models.ImageField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField()
    thumbnail_detail = models.CharField(max_length=30)
    categories = models.ManyToManyField(Category)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_product', kwargs={
            'id':self.title
        })

    def get_absolute_work_url(self):
        return reverse('works', kwargs={
            id:self.categories
        })
