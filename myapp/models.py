from django.db import models
from django.contrib.auth.models import User


class Category_Tag(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name


class RecipeDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category_Tag)
    description = models.TextField(null=True, blank=True)
    ingredient_list = models.TextField(default='Item1')
    introduction = models.TextField(default='Take a bowl.')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, verbose_name="Video", blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(default='separated by comma', max_length=100,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_time']



class TagList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    recipe = models.ForeignKey(RecipeDetail, on_delete=models.CASCADE, default=None)
    hash_tag = models.CharField(max_length=60,null=True, blank=True)

    def __str__(self):
        return self.hash_tag



